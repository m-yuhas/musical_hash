"""MusicalHash class and helper functions."""


from typing import Callable, List, Union
import hashlib
import zlib
import mido
import numpy
import wavio
from ._scales import CHROMATIC_SCALE


DEFAULT_NOTE_DURATION = 0.5
DEFAULT_SAMPLE_RATE = 44100
DEFAULT_TICKS_PER_NOTE = 500
PITCH_STANDARD = 440


HashFunction = Callable[[bytearray], bytearray]


def get_notes_in_scale(all_notes: List[Union[float, int, str]],
                       scale: int) -> List[Union[float, int, str]]:
    """Return a list of all notes in scale, where the notes are chosen from a
    set of all twelve possible semitones.

    Args:
        all_notes: List of strings, integers, or floats that make up the set of
            all twelve semitones.  The list contents could represent notes in
            ABC notation (A, #A, B, ...), frequencies, midi note numbers, etc.
        scale: an integer mask where each '1' bit means the note is present in
            the output scale and a '0' bit means it is not present.  The least
            significant bit always corresponds to the first note in all_notes.

    Returns:
        A list of notes that is a subset of the input all_notes list.

    Raises:
        A ValueError if the scale argument has one or fewer notes or more than
        twelve notes.
    """
    if scale <= 1 or scale > 0xfff:
        raise ValueError(
            'A valid musical scale must include at least two notes and no '
            'more then twelve notes (0x001 to 0xfff)')
    scale_notes = []
    for i, note in enumerate(all_notes):
        if scale & (0x1 << i):
            scale_notes.append(note)
    if len(scale_notes) == 1:
        raise ValueError(
            'Only one note appears in this scale; currently monotonic scales '
            'are not supported')
    return scale_notes


def change_base(number: int, base: int) -> List[int]:
    """Express an integer in another base.

    Args:
        number: The integer to convert.
        base: The base to which to convert number.

    Returns:
        A list of integers, where each integer is a digit in number expressed
        as base. The first element in the list is least significant digit and
        the final element is the most significant digit.
    """
    digits = []
    while number >= base:
        remainder = number % base
        digits.append(remainder)
        number = number // base
    digits.append(number)
    return digits


def pitches_to_tune(pitches: List[float],
                    note_duration: float = DEFAULT_NOTE_DURATION,
                    sample_rate: int = DEFAULT_SAMPLE_RATE) -> numpy.ndarray:
    """Convert a list of pitches to a tune.

    Args:
        pitches: list of floats, each corresponding to a pitch in Hertz.
        note_duration: default note duration in seconds.
        sample_rate: the sample rate for the output tune.

    Returns:
        A numpy array of samples at sample_rate that represents a tune
        constructed by the input list of pitches.

    Raises:
        A ValueError if the note duration or sample rate is less than or equal
        to zero.
    """
    if note_duration <= 0 or sample_rate <= 0:
        raise ValueError(
            'The note duration and sample rate must be positive, '
            'non-zero numbers')
    envelope = numpy.exp(
        0 - numpy.linspace(0, note_duration, int(sample_rate * note_duration)))
    tune = numpy.empty(0)
    for pitch in pitches:
        tune = numpy.append(
            tune,
            envelope * numpy.sin(
                2 * numpy.pi * pitch * numpy.linspace(
                    0, note_duration, int(sample_rate * note_duration))))
    return tune


class MusicalHash:
    """Represents a musical hash of a bytearray.

    # Args
    - *data*: the input data to the musical hash.  Must be a bytearray.
    - *hash_method*: the method to use for hashing.  Can be a string for a
        built-in hash method, or callable for one that is user-defined. A
        user-defined hash method is a Callable object that takes a single
        argument (bytearray) and returns a bytearray, which is the hashed value
        of the input.  The built-in hash methods are: 'md5', 'sha1', 'sha224',
        'sha384', 'sha512', 'blake2b', 'blake2s', 'adler32', 'crc32'.

    # Raises
    A ValueError if an unsupported hash method is specified in the constructor.
    """

    def __init__(self,
                 data: bytearray,
                 hash_method: Union[str, HashFunction]) -> None:
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
                self.hashed_bytes = (builtin_methods[self.hash_method]
                                     ['constructor'](self.data).digest())
            elif builtin_methods[self.hash_method]['module'] == 'zlib':
                self.hashed_bytes = (builtin_methods[self.hash_method]
                                     ['function'](self.data).to_bytes(
                                         4, byteorder='little', signed=False))
            else:
                raise ValueError(
                    'BUG: hash_method: {} not found in builtin_methods map, '
                    'despite already checking the map for its existence. '
                    'Please report this issue to the maintainers of '
                    'musical_hash so it can be fixed'.format(self.hash_method))
        else:
            raise ValueError(
                'The hash_method: {} is not '
                'supported.'.format(self.hash_method))

    def notes(self,
              key: int = CHROMATIC_SCALE,
              sharps: bool = True) -> List[str]:
        """Return the hash as a list of notes ('A', '#A', B, '#B', ... ).

        # Args
        - *key*: integer (see scale constants) corresponding to the musical
            key.
        - *sharps*: boolean True if semitones should be reported as sharps
                (#A) or False if they should be reported as flats (bB).

        # Returns
        A List of string where each element corresponds to a note in the
        musical representation of this hash value.

        # Raises
        A ValueError if the key argument has one or fewer notes or more than
        twelve notes.
        """
        notes = []
        if sharps:
            notes = ['A', '#A', 'B', 'C', '#C', 'D',
                     '#D', 'E', 'F', '#F', 'G', '#G']
        else:
            notes = ['A', 'bB', 'B', 'C', 'bD', 'D',
                     'Eb', 'E', 'F', 'bG', 'G', 'bA']
        scale = get_notes_in_scale(notes, key)
        return [scale[i] for i in
                change_base(int.from_bytes(self.hashed_bytes,
                                           byteorder='little'), len(scale))]

    def samples(self,
                key: int = CHROMATIC_SCALE,
                note_duration: int = DEFAULT_NOTE_DURATION,
                sample_rate: int = DEFAULT_SAMPLE_RATE) -> numpy.ndarray:
        """Return the hash as a numpy array of samples.

        # Args
        - *key*: integer (see scale constants) corresponding to the musical key
        - *note_duration*: duration of each note in seconds
        - *sample_rate*: sample rate for the output audio

        # Returns
        Numpy array of audio samples with sample rate.  The hash will be
        represented in a musical key with each note lasting note_duration
        seconds.

        # Raises
        A ValueError if the key argument has one or fewer notes or more than
        twelve notes or if the sample_rate or note_duration are less than or
        equal to zero.
        """
        if note_duration <= 0 or sample_rate <= 0:
            raise ValueError(
                'Note duration and sample rate must be positive, non-zero '
                'integers')
        scale = get_notes_in_scale(
            [PITCH_STANDARD * (2 ** (n / 12)) for n in range(12)],
            key)
        return pitches_to_tune(
            [scale[i] for i in change_base(
                int.from_bytes(self.hashed_bytes, byteorder='little'),
                len(scale))],
            note_duration,
            sample_rate)

    def wave(self,
             filename: str,
             key: int = CHROMATIC_SCALE,
             note_duration: int = DEFAULT_NOTE_DURATION,
             sample_rate: int = DEFAULT_SAMPLE_RATE) -> None:
        """Returns the hash as a wave file.

        # Args
        - *filename*: file path for the output wave file.
        - *key*: integer (see constants) corresponding to the musical key.
        - *note_duration*: duration of each note in seconds.
        - *sample_rate*: sample rate for the output audio.

        # Raises
        A ValueError if the key argument has one or fewer notes or more than
        twelve notes or if the sample_rate or note_duration are less than or
        equal to zero.
        """
        if filename == '':
            raise FileNotFoundError('Empty filename not permitted')
        wavio.write(
            file=filename,
            data=self.samples(key, note_duration, sample_rate),
            rate=sample_rate,
            sampwidth=2)

    def midi(self,
             filename: str,
             key: int = CHROMATIC_SCALE,
             note_duration: int = DEFAULT_TICKS_PER_NOTE,
             instrument: int = 1) -> None:
        """Returns the hash as a midi file.

        # Args
        - *filename*: file path for the output midi file.
        - *key*: integer (see constants) corresponding to the musical key.
        - *note_duration*: duration of each note in midi ticks.
        - *instrument*: integer between 0 and 128 corresponding to the desired
            midi program.
        """
        if filename == '':
            raise FileNotFoundError('Empty filename not permitted')
        if note_duration <= 0:
            raise ValueError('Note duration must be a positive integer')
        file = mido.MidiFile()
        track = mido.MidiTrack()
        track.append(
            mido.Message('program_change', program=instrument, time=0))
        scale = get_notes_in_scale([69 + n for n in range(12)], key)
        for note in change_base(
                int.from_bytes(self.hashed_bytes, byteorder='little'),
                len(scale)):
            track.append(mido.Message(
                'note_on',
                note=scale[note],
                velocity=127,
                time=0))
            track.append(mido.Message(
                'note_off',
                note=scale[note],
                velocity=127,
                time=note_duration))
        file.tracks.append(track)
        file.save(filename)
