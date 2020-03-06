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

## API Documentation
For the complete API documentation, [click here](doc/api_documentation.md).

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

## Contributing
Suggestions and pull requests are welcome.  If you find a bug and don't have
time to fix it yourself, feel free to open an issue.  Also, I am not an expert
at Music Theory; if you find an error with the way a scale or musical term is
named, please call it out so that I can learn.

## Future Tasks
- TODO: Make a hash that includes chords to decrease the tune length and
    increase the perceived uniqueness of each hash.