"""This module contains tools to convert a hash into a sequence of notes so
that you can "visualize" any given hash. The **MusicalHash** class hashes an
array of bytes with a given hash and can export it as a list of notes, an array
of samples, a wave file, or a midi file.  During conversion, you can choose the
musical key or scale that the resulting "visualization" should use.  The
**get_scale** function can be used to create a scale constant based on a list
of notes (ABC Notation) or you can choose from a predefine scale.  The
following scale constants are included with this module:

# Chromatic Scale
```
CHROMATIC_SCALE
```

# Diatonic Scales
```
A_MAJOR, A_MINOR, A_FLAT_MAJOR, A_FLAT_MINOR, A_SHARP_MINOR, B_MAJOR, B_MINOR,
B_FLAT_MAJOR, B_FLAT_MINOR, C_MAJOR, C_MINOR, C_FLAT_MAJOR, C_SHARP_MAJOR,
C_SHARP_MINOR, D_MAJOR, D_MINOR, D_FLAT_MAJOR, D_FLAT_MINOR, D_SHARP_MINOR,
E_MAJOR, E_MINOR, E_FLAT_MAJOR, E_FLAT_MINOR, E_SHARP_MINOR, F_MAJOR, F_MINOR
F_FLAT_MAJOR, F_SHARP_MAJOR, F_SHARP_MINOR, G_MAJOR, G_MINOR, G_FLAT_MAJOR,
G_SHARP_MAJOR, G_SHARP_MINOR
```

# Pentatonic Scales
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
"""


from ._scales import *
from ._musical_hash import MusicalHash
