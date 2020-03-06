# musical_hash
This module contains tools to convert a hash into a sequence of notes so
that you can "visualize" any given hash. The **MusicalHash** class hashes an
array of bytes with a given hash and can export it as a list of notes, an array
of samples, a wave file, or a midi file.  During conversion, you can choose the
musical key or scale that the resulting "visualization" should use.  The
**get_scale** function can be used to create a scale constant based on a list
of notes (ABC Notation) or you can choose from a predefine scale.  The
following scale constants are included with this module:

__Chromatic Scale__

```
CHROMATIC_SCALE
```

__Diatonic Scales__

```
A_MAJOR, A_MINOR, A_FLAT_MAJOR, A_FLAT_MINOR, A_SHARP_MINOR, B_MAJOR, B_MINOR,
B_FLAT_MAJOR, B_FLAT_MINOR, C_MAJOR, C_MINOR, C_FLAT_MAJOR, C_SHARP_MAJOR,
C_SHARP_MINOR, D_MAJOR, D_MINOR, D_FLAT_MAJOR, D_FLAT_MINOR, D_SHARP_MINOR,
E_MAJOR, E_MINOR, E_FLAT_MAJOR, E_FLAT_MINOR, E_SHARP_MINOR, F_MAJOR, F_MINOR
F_FLAT_MAJOR, F_SHARP_MAJOR, F_SHARP_MINOR, G_MAJOR, G_MINOR, G_FLAT_MAJOR,
G_SHARP_MAJOR, G_SHARP_MINOR
```

__Pentatonic Scales__

```
A_BLUES_MAJOR, A_BLUES_MINOR, A_EGYPTIAN, A_MAJOR_PENTATONIC,
A_MINOR_PENTATONIC, A_SHARP_BLUES_MAJOR, A_SHARP_BLUES_MINOR,
A_SHARP_EGYPTIAN, A_SHARP_MAJOR_PENTATONIC, A_SHARP_MINOR_PENTATONIC,
B_BLUES_MAJOR, B_BLUES_MINOR, B_EGYPTIAN, B_MAJOR_PENTATONIC,
B_MINOR_PENTATONIC, C_BLUES_MAJOR, C_BLUES_MINOR, C_EGYPTIAN,
C_MAJOR_PENTATONIC, C_MINOR_PENTATONIC, C_SHARP_BLUES_MAJOR,
C_SHARP_BLUES_MINOR, C_SHARP_EGYPTIAN, C_SHARP_MAJOR_PENTATONIC,
C_SHARP_MINOR_PENTATONIC, D_BLUES_MAJOR, D_BLUES_MINOR, D_EGYPTIAN,
D_MAJOR_PENTATONIC, D_MINOR_PENTATONIC, E_FLAT_BLUES_MAJOR, E_FLAT_BLUES_MINOR,
E_FLAT_EGYPTIAN, E_FLAT_MAJOR_PENTATONIC, E_FLAT_MINOR_PENTATONIC,
E_BLUES_MAJOR, E_BLUES_MINOR, E_EGYPTIAN, E_MAJOR_PENTATONIC,
E_MINOR_PENTATONIC, F_BLUES_MAJOR, F_BLUES_MINOR, F_EGYPTIAN,
F_MAJOR_PENTATONIC, F_MINOR_PENTATONIC, F_SHARP_BLUES_MAJOR,
F_SHARP_BLUES_MINOR, F_SHARP_EGYPTIAN, F_SHARP_MAJOR_PENTATONIC,
F_SHARP_MINOR_PENTATONIC, G_BLUES_MAJOR, G_BLUES_MINOR, G_EGYPTIAN,
G_MAJOR_PENTATONIC, G_MINOR_PENTATONIC, G_SHARP_BLUES_MAJOR,
G_SHARP_BLUES_MINOR, G_SHARP_EGYPTIAN, G_SHARP_MAJOR_PENTATONIC,
G_SHARP_MINOR_PENTATONIC
```

# MusicalHash
```python
MusicalHash(self, data: bytearray, hash_method: Union[str, Callable[[bytearray], bytearray]]) -> None
```
Represents a musical hash of a bytearray.

__Args__

- *data*: the input data to the musical hash.  Must be a bytearray.
- *hash_method*: the method to use for hashing.  Can be a string for a
    built-in hash method, or callable for one that is user-defined. A
    user-defined hash method is a Callable object that takes a single
    argument (bytearray) and returns a bytearray, which is the hashed value
    of the input.  The built-in hash methods are: 'md5', 'sha1', 'sha224',
    'sha384', 'sha512', 'blake2b', 'blake2s', 'adler32', 'crc32'.

__Raises__

A ValueError if an unsupported hash method is specified in the constructor.

## notes
```python
MusicalHash.notes(self, key: int = 4095, sharps: bool = True) -> List[str]
```
Return the hash as a list of notes ('A', '#A', B, '#B', ... ).

__Args__

- *key*: integer (see scale constants) corresponding to the musical
    key.
- *sharps*: boolean True if semitones should be reported as sharps
        (#A) or False if they should be reported as flats (bB).

__Returns__

A List of string where each element corresponds to a note in the
musical representation of this hash value.

__Raises__

A ValueError if the key argument has one or fewer notes or more than
twelve notes.

## samples
```python
MusicalHash.samples(self, key: int = 4095, note_duration: int = 0.5, sample_rate: int = 44100) -> numpy.ndarray
```
Return the hash as a numpy array of samples.

__Args__

- *key*: integer (see scale constants) corresponding to the musical key
- *note_duration*: duration of each note in seconds
- *sample_rate*: sample rate for the output audio

__Returns__

Numpy array of audio samples with sample rate.  The hash will be
represented in a musical key with each note lasting note_duration
seconds.

__Raises__

A ValueError if the key argument has one or fewer notes or more than
twelve notes or if the sample_rate or note_duration are less than or
equal to zero.

## wave
```python
MusicalHash.wave(self, filename: str, key: int = 4095, note_duration: int = 0.5, sample_rate: int = 44100) -> None
```
Returns the hash as a wave file.

__Args__

- *filename*: file path for the output wave file.
- *key*: integer (see constants) corresponding to the musical key.
- *note_duration*: duration of each note in seconds.
- *sample_rate*: sample rate for the output audio.

__Raises__

A ValueError if the key argument has one or fewer notes or more than
twelve notes or if the sample_rate or note_duration are less than or
equal to zero.

## midi
```python
MusicalHash.midi(self, filename: str, key: int = 4095, note_duration: int = 500, instrument: int = 1) -> None
```
Returns the hash as a midi file.

__Args__

- *filename*: file path for the output midi file.
- *key*: integer (see constants) corresponding to the musical key.
- *note_duration*: duration of each note in midi ticks.
- *instrument*: integer between 0 and 128 corresponding to the desired
    midi program.

# get_scale
```python
get_scale(notes: List[str]) -> int
```
Convert a list of notes to a scale constant.

__Args__

- *notes*: list of notes in the scale.  This should be a list of string
    where each string is a note ABC notation. Sharps should be
    represented with a pound sign preceding the note e.g. '#A' and flats
    should be represented with a lower case b preceding the note e.g. 'bB'.

__Returns__

An integer mask used to represent a musical key or scale as an argument to
any of the MusicalHash methods.

__Raises__

A ValueError if an invalid string is included in the input list.

