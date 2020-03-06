"""Scale constants and functions to help with the creation of new scales."""


from typing import List


# Chromatic Scale
CHROMATIC_SCALE = 0xfff


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
C_BLUES_MAJOR = 0x1a5
C_BLUES_MINOR = 0xc62
C_EGYPTIAN = 0x94a
C_MAJOR_PENTATONIC = 0x48d
C_MINOR_PENTATONIC = 0x962
C_SHARP_BLUES_MAJOR = 0x34a
C_SHARP_BLUES_MINOR = 0xa51
C_SHARP_EGYPTIAN = 0x8c5
C_SHARP_MAJOR_PENTATONIC = 0x31a
C_SHARP_MINOR_PENTATONIC = 0x8d1
D_BLUES_MAJOR = 0x2a5
D_BLUES_MINOR = 0x329
D_EGYPTIAN = 0x4a3
D_MAJOR_PENTATONIC = 0x295
D_MINOR_PENTATONIC = 0x4a9
E_FLAT_BLUES_MAJOR = 0x54a
E_FLAT_BLUES_MINOR = 0xa52
E_FLAT_EGYPTIAN = 0x946
E_FLAT_MAJOR_PENTATONIC = 0x52a
E_FLAT_MINOR_PENTATONIC = 0x952
E_BLUES_MAJOR = 0xac5
E_BLUES_MINOR = 0x629
E_EGYPTIAN = 0x4a5
E_MAJOR_PENTATONIC = 0x295
E_MINOR_PENTATONIC = 0x4a9
F_BLUES_MAJOR = 0x1a3
F_BLUES_MINOR = 0xc52
F_EGYPTIAN = 0x94a
F_MAJOR_PENTATONIC = 0x18b
F_MINOR_PENTATONIC = 0x952
F_SHARP_BLUES_MAJOR = 0x346
F_SHARP_BLUES_MINOR = 0xa31
F_SHARP_EGYPTIAN = 0x8a5
F_SHARP_MAJOR_PENTATONIC = 0x316
F_SHARP_MINOR_PENTATONIC = 0x8b1
G_BLUES_MAJOR = 0x2a5
G_BLUES_MINOR = 0x529
G_EGYPTIAN = 0x463
G_MAJOR_PENTATONIC = 0x28d
G_MINOR_PENTATONIC = 0x469
G_SHARP_BLUES_MAJOR = 0x54a
G_SHARP_BLUES_MINOR = 0xa52
G_SHARP_EGYPTIAN = 0x8c6
G_SHARP_MAJOR_PENTATONIC = 0x51a
G_SHARP_MINOR_PENTATONIC = 0x8d2


def get_scale(notes: List[str]) -> int:
    """Convert a list of notes to a scale constant.

    # Args
    - *notes*: list of notes in the scale.  This should be a list of string
        where each string is a note ABC notation. Sharps should be
        represented with a pound sign preceding the note e.g. '#A' and flats
        should be represented with a lower case b preceding the note e.g. 'bB'.

    # Returns
    An integer mask used to represent a musical key or scale as an argument to
    any of the MusicalHash methods.

    # Raises
    A ValueError if an invalid string is included in the input list.
    """
    note_map = {'A': 0x1,
                '#A': 0x2, 'bB': 0x2,
                'B': 0x4,
                'C': 0x8,
                '#C': 0x10, 'bD': 0x10,
                'D': 0x20,
                '#D': 0x40, 'bE': 0x40,
                'E': 0x80,
                'F': 0x100,
                '#F': 0x200, 'bG': 0x200,
                'G': 0x400,
                '#G': 0x800, 'bA': 0x800}
    scale = 0x0
    for note in notes:
        try:
            scale |= note_map[note]
        except KeyError:
            raise ValueError(
                'The string {} is not a valid musical note'.format(note))
    return scale
