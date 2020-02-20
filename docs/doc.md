# musical_hash
This is the __init__ file.  Let's see where this docstring ends up in the
autodocker.
# MusicalHash
```python
MusicalHash(self, data: bytearray, hash_method: Union[str, Callable[[bytearray], bytearray]]) -> None
```
Represents a musical hash of a bytearray.

Attributes:
    data: the input data to the musical hash.  Must be a bytearray
    hash_method: the method to use for hashing.  Can be a string
        for a built-in hash method, or callable for one that is
        user-defined
    hashed_bytes: the hashed bytes

## samples
```python
MusicalHash.samples(self, key: int = 4095, note_duration: int = 0.5, sample_rate: int = 44100) -> numpy.ndarray
```
Return the hash as a numpy array of samples.

Args:
    key: integer (see constants) corresponding to the musical key
    note_duration: duration of each note in seconds
    sample_rate: sample rate for the output audio

Returns:
    Numpy array of audio samples with <sample rate>.  The hash will be
    represented in <key> with each note lasting <note_duration>
    seconds.

## wave
```python
MusicalHash.wave(self, filename: str, key: int = 4095, note_duration: int = 0.5, sample_rate: int = 44100) -> None
```
Returns the hash as a wave file.

Args:
    filename: file path for the output wave file.
    key: integer (see constants) corresponding to the musical key
    note_duration: duration of each note in seconds
    sample_rate: sample rate for the output audio

## midi
```python
MusicalHash.midi(self, filename: str, key: int = 4095, note_duration: int = 1000, instrument: int = 1) -> None
```
Returns the hash as a midi file.

Args:
    filename: file path for the output midi file.
    key: integer (see constants) corresponding to the musical key
    note_duration: duration of each note in midi ticks
    volume: number between 0 and 1 where 1 is maximum volume and 0 is
        mute

# musical_hash._scales
Musical constants used while converting between bytes and melodies.

This module has has three basic groupings:

1.) File IO Constants - constants associated with sampling rate, bit depth, and
    other options associated with sound quality.

2.) Translation Constants - constants associated with the operation of
    converting bytes to a melody.

3.) Diatonic Scales - each constant is an integer that represents a particular
    diatonic scale.  The first semitone in the octave (usually A440) is
    represented by the least significant bit and the highest semitone (G before
    A880) is represented by the most significant bit.  Each bit that is one
    indicates that semitone is present in the scale, therefore the Hamming
    distance between any diatonic scale constant and 0x00 is always seven.

4.) Pentatonic Scales - each constant is an integer constructed according to
    the same rules as the diatonic scale constants.  The difference is now that
    the Hamming distance between a pentatonic scale constant and 0x00 is always
    five.

