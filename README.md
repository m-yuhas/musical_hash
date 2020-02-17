# Musical Hash
## Introduction
Just as Random Art provides a method to visualize RSA keys, Musical Hash
provides a method to "visualize" the output of a hash function in the audio
domain.
## Quick Start
* Clone this repository:

```
git clone https://github.com/m-yuhas/musical_hash.git
```

* Build the package:

```
python setup.py sdist
```

* Install the package on the desired virtual environment:

```
python -m pip install musical_hash-x.y.z.tar.gz
```

* Try it:

```
import musical_hash
hash = musical_hash.MusicalHash(b'Hello World!', 'md5')
hash.wave('hash.wav', key=musical_hash.A_BLUES_MAJOR)
hash.midi('hash.mid', key=musical_hash.A_BLUES_MAJOR)
```

## Theory of Operation
In western music there are twelve semitones in an octave. The first note of the
subsequent octave is the first harmonic of the first note of the previous
octave.  Thus we will consider a single octave as the universe of all notes
available to "visualize" a sequence of bytes.  Most pieces of music are written
in a specific key, which is a subset of all available notes.  Within a single
octave, each key has a finite number of notes, so if we consider the sequence of
bytes as an integer, we can find that integer's representation in a base equal
to the number of notes in a key.  We then assign each digit of this
representation a musical note.  This package comes with many diatonic and
pentatonic keys as constants.

## Dependencies
Only Python version 3.5 and greater are supported.  This package should run on
any POSIX system as well as Windows 7 and greater.

The following Pypi packages are required:
* mido
* numpy
* wavio

## API
### Classes
#### MusicalHash(data: bytearray, hash_method: str)
MusicalHash represents a hash of some bytearray. The constructor takes the
following arguments:
* data : The input to the hashing algorithm, must be a bytearray 
* hash_method : A string or a callable object that returns a bytearray.  If a string is provided, it must be one of the following hashing algorithms:
    - md5
    - sha1
    - sha224
    - sha384
    - sha512
    - blake2b
    - blake2s
    - adler32
    - crc32

Class attributes:
* data: the input data to the musical hash.  Must be a bytearray
* hash_method: the method to use for hashing.  Can be a string for a built-in hash method, or callable for one that is user-defined
* hashed_bytes: the hashed bytes

##### samples(key: int = CHROMATIC_SCALE, note_duration: int = DEFAULT_NOTE_DURATION, sample_rate: int = DEFAULT_SAMPLE_RATE) -> numpy.ndarray:
Return the hash as a numpy array of samples.
        
Args:
* key: integer (see constants) corresponding to the musical key
* note_duration: duration of each note in seconds
* sample_rate: sample rate for the output audio

Returns:
* Numpy array of audio samples with <sample rate>.  The hash will be represented in <key> with each note lasting <note_duration> seconds.

##### wave(filename: str, key: int = CHROMATIC_SCALE, note_duration: int = DEFAULT_NOTE_DURATION, sample_rate: int = DEFAULT_SAMPLE_RATE) -> None:
Returns the hash as a wave file.

Args:
* filename: file path for the output wave file.
* key: integer (see constants) corresponding to the musical key
* note_duration: duration of each note in seconds
* sample_rate: sample rate for the output audio

##### midi(filename: str, key: int = CHROMATIC_SCALE, note_duration: int = DEFAULT_TICKS_PER_NOTE, volume: float = 0.5, instrument: int = 1) -> None:
Returns the hash as a midi file.

Args:
* filename: file path for the output midi file.
* key: integer (see constants) corresponding to the musical key
* note_duration: duration of each note in midi ticks
* volume: number between 0 and 1 where 1 is maximum volume and 0 is mute