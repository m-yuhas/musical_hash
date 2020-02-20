"""Utilities for converting a melody into a sequence of bytes.

After converting a hashed value into a melody, it may sometimes be desirable to
convert it back into bytes.  This module contains utilities to perform this
conversion for wave and midi sound formats.

def file_to_song(filename: str) -> List[float]:
    wave = _wavio.read(filename)
    window = _np.hanning(int(wave.rate/4))
    segments = []
    i = 0
    while i < w.data.size:
        segmets.append(
            _np.mulitply(_np.squeeze(wave.data[i:i+window.size]), window))
        i += window.size
    tones = [PITCH_STANDARD/4 * (2 ** (n / 12)) for n in range(12)]
    notes = []
    for tone in tones:
        note = _np.zeros(note_duration * sample_rate)
        for harmonic in range(1, 5):
            note = _np.add(
                _np.sin(
                    2 * _np.pi * tone * harmonic * _np.linspace(
                        0, note_duration, sample_rate)), note)
        notes.append(note)
    fftnotes = _np.zeros(12, )
    for seg in segments:
        fftlength = _next_power_of_two(seg.size)
        segmentfft = _np.fft(seg, n=fftlength)
"""


def _next_power_of_two(number: int) -> int:
    """Find the next highest power of two.

    Args:
        n: any integer

    Returns:
        The next highest power of 2 after <n>.  If <n> is a power of 2, then
        <n> is returned.
    """
    power = 1
    while power < number:
        power <<= 1
    return power
