"""Implements a musical hash in Python.

Convert a hash into a sequence of notes so that you can "visualize" any given
hash.  Conversely, take a sequence of notes and turn them into the bytes of a
hash to use during computations.
"""


import hashlib
import numpy as _np
import wavio as _wavio
import zlib
from constants import *
from typing import Callable, List
from locale import str


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
            'asler32': {'module': 'zlib', 'function': zlib.adler32},
            'crc32': {'module': 'zlib', 'function': zlib.crc32}}
        if callable(self.hash_method):
            self.hashed_bytes = self.hash_method(data)
        elif self.hash_method.lower() in builtin_methods:
            if builtin_methods[self.hash_method]['module'] == 'hashlib':
                self.hashed_bytes = builtin_methods[self.hash_method]
                    ['constructor'](self.data).digest()
            elif builtin_methods[self.hash_method]['module'] == 'zlib':
                self.hashed_bytes = builtin_methods[self.hash_method]
                    ['function'](self.data)
            else:
                raise ValueError(
                    'BUG: hash_method: {} not found in builtin_methods map, '
                    'despite already checking the map for its existence. '
                    'Please report this issue to the maintainers of '
                    'musical_hash so it can be fixed'.format(self.hash_method))
        else:
            raise ValueError(
                'The hash_method: {} is not supported.'.format(self.has_method))
            

def _get_scale_frequencies(scale: int) -> List[float]:
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


def _pitch_list_to_tune(pitches: List[float],
                       note_duration: float = DEFAULT_NOTE_DURATION,
                       sample_rate: int = DEFAULT_SAMPLE_RATE) -> _np.ndarray:
    """Convert a list of pitches to a tune.
    
    Args:
        pitches: list of floats, each corresponding to a pitch in hertz.
        note_duration: default note duration in seconds.
        sample_rate: the sample rate for the output tune.

    Returns:
        A numpy array of samples at <sample_rate> that represents a tune
        constructed by the input list of pitches.
    """
    song = _np.empty(0)
    for pitch in pitches:
        song = _np.append(
            song,
            _np.sin(
                2 * _np.pi * pitch * _np.linspace(
                    0, note_duration, sample_rate)))
    #b, a = scipy.signal.butter(1, 10000 / DEFAULT_SAMPLE_RATE, 'low')
    #song = scipy.signal.filtfilt(b, a, song)
    return song


def _bytes_to_pitches(bytes: bytearray,
                     key: int = CHROMATIC_SCALE) -> List[float]:
    """Convert a bytearray to a list of pitches.

    Args:
        bytes: the input bytearray
        key: the musical key for the output series of pitches.

    Returns:
        A list of floats corresponding to musical notes.  The notes are selected
        by performing a change of base on the bytearray to the number of notes
        in the selected musical key.
    """
    scale = _get_scale_frequencies(key)
    pitches = []
    data = int.from_bytes(bytes, byteorder='big')
    while data > len(scale):
        remainder = data % len(scale)
        pitches.append(scale[remainder])
        data = int((data - remainder) / len(scale))
    pitches.append(scale[data])
    return pitches


def tune_to_wave(tune: _np.ndarray, filename: str) -> None:
    """Write a tune to a wave file.

    Args:
        tune: numpy array of samples of the tune to write to file
        filename: the name of the file to write
    """
    #with wave.open(filename, 'w') as file:
    #    file.setnchannels(1)
    #    file.setsampwidth(2)
    #    file.setframerate(DEFAULT_SAMPLE_RATE)
    #    for sample in numpy.nditer(song):
    #        file.writeframesraw(struct.pack('<h', int(sample * 10000)))
    pass




def musical_hash(bytes: bytearray,
                 algorithm,
                 key: int = CHROMATIC_SCALE,
                 note_duration: int = DEFAULT_NOTE_DURATION,
                 sample_rate: int = DEFAULT_SAMPLE_RATE) -> _np.ndarray:
    hashed_bytes = algorithm(bytes).digest()
    pitches = _bytes_to_pitches(hashed_bytes, key)
    return _pitch_list_to_song(pitches, note_duration, sample_rate)


def musical_md5(bytes: bytearray,
                key: int = CHROMATIC_SCALE,
                note_duration: int = DEFAULT_NOTE_DURATION,
                sample_rate: int = DEFAULT_SAMPLE_RATE):
    return musical_hash(bytes, md5, key, note_duration, sample_rate)


def musical_sha1():
    pass


def musical_sha224():
    pass


def musical_sha384():
    pass


def musical_sha512():
    pass


def musical_blake2b():
    pass


def musical_blake2s():
    pass


def musical_crc32():
    pass
