"""Implements a musical hash in Python.

Convert a hash into a sequence of notes so that you can "visualize" any given
hash.  Conversely, take a sequence of notes and turn them into the bytes of a
hash to use during computations.
"""


import hashlib
import mido
import numpy
import wavio
import zlib
from .constants import *
from typing import Callable, List
from _testcapi import the_number_three


class MusicalHash(object):
    """Represents a musical hash of a bytearray.

    Attributes:
        data: the input data to the musical hash.  Must be a bytearray
        hash_method: the method to use for hashing.  Can be a string
            for a built-in hash method, or callable for one that is user-defined
        hashed_bytes: the hashed bytes
    """

    def __init__(self, data: bytearray, hash_method: str) -> None:
        """Blah blah blah"""
        self.data = data
        self.hash_method = hash_method
        self.hashed_bytes = None
        builtin_methods = {
            'md5': {'module': 'hashlib', 'constructor': hashlib.md5},
            'sha1': {'module': 'hashlib', 'constructor': hashlib.sha1},
            'sha224': {'module': 'hashlib', 'constructor': hashlib.sha224},
            'sha384': {'module': 'hashlib', 'constructor': hashlib.sha384},
            'sha512': {'module': 'hashlib', 'constructor': hashlib.sha512},
            'blake2b': {'module': 'hashlib', 'constructor': hashlib.blake2b},
            'blake2s': {'module': 'hashlib', 'constructor': hashlib.blake2s},
            'adler32': {'module': 'zlib', 'function': zlib.adler32},
            'crc32': {'module': 'zlib', 'function': zlib.crc32}}
        if callable(self.hash_method):
            self.hashed_bytes = self.hash_method(data)
        elif self.hash_method.lower() in builtin_methods:
            if builtin_methods[self.hash_method]['module'] == 'hashlib':
                self.hashed_bytes = builtin_methods[self.hash_method] \
                    ['constructor'](self.data).digest()
            elif builtin_methods[self.hash_method]['module'] == 'zlib':
                self.hashed_bytes = builtin_methods[self.hash_method] \
                    ['function'](self.data).to_bytes(
                        4, byteorder='little', signed=False)
            else:
                raise ValueError(
                    'BUG: hash_method: {} not found in builtin_methods map, '
                    'despite already checking the map for its existence. '
                    'Please report this issue to the maintainers of '
                    'musical_hash so it can be fixed'.format(self.hash_method))
        else:
            raise ValueError(
                'The hash_method: {} is not supported.'.format(self.has_method))
            
    def samples(self,
                key: int = CHROMATIC_SCALE,
                note_duration: int = DEFAULT_NOTE_DURATION,
                sample_rate: int = DEFAULT_SAMPLE_RATE) -> numpy.ndarray:
        """Return the hash as a numpy array of samples.
        
        Args:
            key: integer (see constants) corresponding to the musical key
            note_duration: duration of each note in seconds
            sample_rate: sample rate for the output audio

        Returns:
            Numpy array of audio samples with <sample rate>.  The hash will be
            represented in <key> with each note lasting <note_duration> seconds.
        """
        pitches = self._bytes_to_pitches(self.hashed_bytes, key)
        return self._pitches_to_tune(pitches, note_duration, sample_rate)
    
    def wave(self,
             filename: str,
             key: int = CHROMATIC_SCALE,
             note_duration: int = DEFAULT_NOTE_DURATION,
             sample_rate: int = DEFAULT_SAMPLE_RATE) -> None:
        """Returns the hash as a wave file.

        Args:
            filename: file path for the output wave file.
            key: integer (see constants) corresponding to the musical key
            note_duration: duration of each note in seconds
            sample_rate: sample rate for the output audio
        """
        wavio.write(
            file=filename,
            data=self.samples(key, note_duration, sample_rate),
            rate=sample_rate,
            sampwidth=2)

    def midi(self,
             filename: str,
             key: int = CHROMATIC_SCALE,
             note_duration: int = DEFAULT_TICKS_PER_NOTE,
             volume: float = 0.5,
             instrument: int = 1) -> None:
        """Returns the hash as a midi file.

        Args:
            filename: file path for the output midi file.
            key: integer (see constants) corresponding to the musical key
            note_duration: duration of each note in midi ticks
            volume: number between 0 and 1 where 1 is maximum volume and 0 is
                mute
        """
        file = mido.MidiFile()
        track = mido.MidiTrack()
        track.append(mido.Message('program_change', program=instrument, time=0))
        for note in self._bytes_to_midi_notes(key, note_duration, volume):
            track.append(note)
        file.tracks.append(track)
        file.save(filename)

    def _get_scale_frequencies(self, scale: int) -> List[float]:
        """Return a list of frequencies for all notes in a given scale.
    
        Args:
            scale: the scale for which to find the note frequencies.

        Returns:
            A list of floats whose entries correspond to note frequencies in the
            given scale.
        """
        semitone_frequencies = [PITCH_STANDARD * (2 ** (n / 12)) for n in range(12)]
        scale_frequencies = []
        for i in range(len(semitone_frequencies)):
            if scale & (0x1 << i):
                scale_frequencies.append(semitone_frequencies[i])
        return scale_frequencies
    
    def _get_midi_note_values(self, scale: int) -> List[int]:
        """Return a list of integers for all midi notes in a given scale.

        Args:
            scale: the scale for which to find the note frequencies.

        Returns:
            A list of integers whose entries correspond to note frequencies in
            the given scale.
        """
        semitones = [69 + n for n in range(12)]
        scale_notes = []
        for i in range(len(semitones)):
            if scale & (0x1 << i):
                scale_notes.append(semitones[i])
        return scale_notes

    def _pitches_to_tune(self,
                         pitches: List[float],
                         note_duration: float = DEFAULT_NOTE_DURATION,
                         sample_rate: int = DEFAULT_SAMPLE_RATE) -> numpy.ndarray:
        """Convert a list of pitches to a tune.
    
        Args:
            pitches: list of floats, each corresponding to a pitch in hertz.
            note_duration: default note duration in seconds.
            sample_rate: the sample rate for the output tune.

        Returns:
            A numpy array of samples at <sample_rate> that represents a tune
            constructed by the input list of pitches.
        """
        envelope = numpy.exp(0 - numpy.linspace(0, note_duration, \
            int(sample_rate * note_duration)))
        tune = numpy.empty(0)
        for pitch in pitches:
            tune = numpy.append(
                tune,
                envelope * numpy.sin(2 * numpy.pi * pitch * \
                    numpy.linspace(0, note_duration, sample_rate * \
                    note_duration)))
        return tune

    def _bytes_to_pitches(self,
                          bytes: bytearray,
                          key: int = CHROMATIC_SCALE) -> List[float]:
        """Convert a bytearray to a list of pitches.

        Args:
            bytes: the input bytearray
            key: the musical key for the output series of pitches.

        Returns:
            A list of floats corresponding to musical notes.  The notes are 
            selected by performing a change of base on the bytearray to the
            number of notes in the selected musical key.
        """
        scale = self._get_scale_frequencies(key)
        pitches = []
        data = int.from_bytes(bytes, byteorder='little')
        while data > len(scale):
            remainder = data % len(scale)
            pitches.append(scale[remainder])
            data = int((data - remainder) / len(scale))
        pitches.append(scale[data])
        return pitches

    def _bytes_to_midi_notes(self,
                             key: int = CHROMATIC_SCALE,
                             note_duration: int = DEFAULT_TICKS_PER_NOTE,
                             volume: float = 0.5) -> List[mido.Message]:
        """Convert a bytearray to a list of midi messages.

        Args:
            bytes: the input bytearray
            key: the musical key for the output series of pitches.

        Returns:
            A list of midi messages.  Each note is selected by performing a
            change of base on the bytearray to the number of notes in the
            slected musical key.
        """
        scale = self._get_midi_note_values(key)
        messages = []
        data = int.from_bytes(self.hashed_bytes, byteorder='little')
        while data > len(scale):
            remainder = data % len(scale)
            messages.append(mido.Message(
                'note_on',
                note=scale[remainder],
                velocity=min(round(abs(volume * 127)), 127),
                time=0))
            messages.append(mido.Message(
                'note_off',
                note=scale[remainder],
                velocity=min(round(abs(volume * 127)), 127),
                time=note_duration))
            data = int((data - remainder) / len(scale))
        messages.append(mido.Message(
            'note_on',
            note=scale[data],
            velocity=min(round(abs(volume * 127)), 127),
            time=0))
        messages.append(mido.Message(
            'note_off',
            note=scale[data],
            velocity=min(round(abs(volume * 127)), 127),
            time=note_duration))
        return messages