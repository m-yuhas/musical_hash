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

## notes
```python
MusicalHash.notes(self, key: int = 4095, sharps: bool = True) -> List[str]
```
Return the hash as a list of notes ('A', '#A', B, '#B', ... ).

Args:
    key: integer (see constants) corresponding to the musical key.
    sharps: boolean True if semitones should be reported as sharps
        (#<note) or False if they should be reported as flats
        (b<note>).

Returns:
    A List of string where each element corresponds to a note in the
    musical representation of this hash value.

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

# get_scale
```python
get_scale(notes: List[str]) -> int
```
Convert a list of notes to a scale constant.
