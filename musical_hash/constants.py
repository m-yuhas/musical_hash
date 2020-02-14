"""Musical constants used while converting between bytes and melodies.

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

4.) Pentatonic Scales - each constant is an integer constructed according to the
    same rules as the diatonic scale constants.  The difference is now that the
    Hamming distance between a pentatonic scale constant and 0x00 is always
    five.
"""


# File IO Constants
DEFAULT_SAMPLE_RATE = 44100


# Pitch Standard and Chromatic Scale
PITCH_STANDARD = 440
CHROMATIC_SCALE = 0xfff
DEFAULT_NOTE_DURATION = 1


# Diatonic Scales
A_MAJOR = 0xab5
A_MINOR = 0x5ad
A_FLAT_MAJOR = 0xd5a
A_FLAT_MINOR = 0xad6
A_SHARP_MINOR = 0xb5a
B_MAJOR = 0xad6
B_MINOR = 0x6b5
B_FLAT_MAJOR = 0x56b
B_FLAT_MINOR = 0xb5a
C_MAJOR = 0x5ad
C_MINOR = 0xd6a
C_FLAT_MAJOR = 0xad6
C_SHARP_MAJOR = 0xb5a
C_SHARP_MINOR = 0xad5
D_MAJOR = 0x6b5
D_MINOR = 0x5ab
D_FLAT_MAJOR = 0xb5a
D_FLAT_MINOR = 0xad5
D_SHARP_MINOR = 0xb56
E_MAJOR = 0xad5
E_MINOR = 0x6ad
E_FLAT_MAJOR = 0xd6a
E_FLAT_MINOR = 0xb56
E_SHARP_MINOR = 0xd5a
F_MAJOR = 0x5ab
F_MINOR = 0xd5a
F_FLAT_MAJOR = 0xad5
F_SHARP_MAJOR = 0xb56
F_SHARP_MINOR = 0xab5
G_MAJOR = 0x6ad
G_MINOR = 0x56b
G_FLAT_MAJOR = 0xb56
G_SHARP_MAJOR = 0xd5a
G_SHARP_MINOR = 0xad6


# Pentatonic Scales
A_BLUES_MAJOR = 0x2a5
A_BLUES_MINOR = 0x529
A_EGYPTIAN = 0x4a5
A_MAJOR_PENTATONIC = 0x295
A_MINOR_PENTATONIC = 0x4a9
A_SHARP_BLUES_MAJOR = 0x163
A_SHARP_BLUES_MINOR = 0xa52
A_SHARP_EGYPTIAN = 0x94a
A_SHARP_MAJOR_PENTATONIC = 0x14b
A_SHARP_MINOR_PENTATONIC = 0x952
B_BLUES_MAJOR = 0x8d2
B_BLUES_MINOR = 0x631
B_EGYPTIAN = 0x4a5
B_MAJOR_PENTATONIC = 0x296
B_MINOR_PENTATONIC = 0x4b1
C_MAJOR_PENTATONIC = 0x48d
C_BLUES_MAJOR = 0x1a5
C_SHARP_BLUES_MAJOR = 0x34a
C_SHARP_MAJOR_PENTATONIC = 0x31a
D_BLUES_MAJOR = 0x2a5
D_MAJOR_PENTATONIC = 0x295
F_BLUES_MINOR = 0xc52
F_EGYPTIAN = 0x94a
F_MINOR_PENTATONIC = 0x952
F_SHARP_BLUES_MINOR = 0xa31
F_SHARP_EGYPTIAN = 0x8a5
F_SHARP_MINOR_PENTATONIC = 0x8b1
G_BLUES_MINOR = 0x529
G_EGYPTIAN = 0x463
G_MINOR_PENTATONIC = 0x469
G_SHARP_BLUES_MAJOR = 0x54a
G_SHARP_BLUES_MINOR = 0xa52
G_SHARP_EGYPTIAN = 0x8c6
G_SHARP_MAJOR_PENTATONIC = 0x51a
G_SHARP_MINOR_PENTATONIC = 0x8d2