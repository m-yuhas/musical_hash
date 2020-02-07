#!/usr/bin/env python3


"""Implements a musical hash in Python.

Convert a hash into a sequence of notes so that you can "visualize" any given
hash.  Conversely, take a sequence of notes and turn them into the bytes of a
hash to use during computations.
"""


import hashlib as _hashlib
import numpy as _np
import wavio as _wavio
from typing import Callable, List


# File IO Constants
DEFAULT_SAMPLE_RATE = 44100
DEFAULT_NOTE_DURATION = 1


# Pitch Standard and Chromatic Scale
PITCH_STANDARD = 440
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
A_EGYPTION = 0x4a5
A_MAJOR_PENTATONIC = 0x295
A_MINOR_PENTATONIC = 0x4a9
C_MAJOR_PENTATONIC = 0x48d
C_BLUES_MAJOR = 0x1a5
F_BLUES_MINOR = 0xc52
F_EGYPTIAN = 0x94a
F_MINOR_PENTATONIC = 0x952
F_SHARP_BLUES_MINOR = 0xa31
F_SHARP_EGYPTION = 0x8a5
F_SHARP_MINOR_PENTATONIC = 0x8b1
G_SHARP_BLUES_MAJOR = 0x54a
G_SHARP_MAJOR_PENTATONIC = 0x51a



def get_scale_frequencies(scale: int) -> List[float]:
    semitone_frequencies = [PITCH_STANDARD * (2 ** (n / 12)) for n in range(12)]
    scale_frequencies = []
    for i in range(len(semitone_frequencies)):
        if scale & (0x1 << i):
            scale_frequencies.append(semitone_frequencies[i])
    return scale_frequencies

def pitch_list_to_song(pitches: List[float],
                       note_duration: float = 1,
                       sample_rate: int = DEFAULT_SAMPLE_RATE) -> ndarray:
    song = empty(0)
    for pitch in pitches:
        song = append(song, sin(2 * numpy.pi * pitch * linspace(0, note_duration, sample_rate)))
    #b, a = scipy.signal.butter(1, 10000 / DEFAULT_SAMPLE_RATE, 'low')
    #song = scipy.signal.filtfilt(b, a, song)
    return song

def bytes_to_pitches(bytes: bytearray,
                     key: int = CHROMATIC_SCALE) -> List[float]:
    scale = get_scale_frequencies(key)
    pitches = []
    data = int.from_bytes(bytes, byteorder='big')
    while data > len(scale):
        remainder = data % len(scale)
        pitches.append(scale[remainder])
        data = int((data - remainder) / len(scale))
    pitches.append(scale[data])
    return pitches

def song_to_bytes(song: List[float]) -> bytearray:
    pass

def song_to_file(song: ndarray, filename: str) -> None:
    with wave.open(filename, 'w') as file:
        file.setnchannels(1)
        file.setsampwidth(2)
        file.setframerate(DEFAULT_SAMPLE_RATE)
        for sample in numpy.nditer(song):
            file.writeframesraw(struct.pack('<h', int(sample * 10000)))

def file_to_song(filename: str) -> List[float]:
    wave = wavio.read(filename)
    window = numpy.hanning(int(wave.rate/4))
    segments = []
    i = 0
    while i < w.data.size:
        segmets.append(
            numpy.mulitply(numpy.squeeze(wave.data[i:i+window.size]), window))
        i += window.size
    tones = [PITCH_STANDARD/4 * (2 ** (n / 12)) for n in range(12)]
    notes = []
    for tone in tones:
        note = numpy.zeros(note_duration * sample_rate)
        for harmonic in range(1,5):
            note = numpy.add(sin(2 * numpy.pi * tone * harmonic * linspace(0, note_duration, sample_rate)), note)
        notes.append(note)
    fftnotes = numpy.zeros(12, )
    for seg in segments:
        fftlength = next_power_of_two(seg.size)
        segmentfft = numpy.fft(seg, n=fftlength)
        
        
def next_power_of_two(n):
    p = 1
    while p < n:
        p <<= 1
    return p
        
        

def musical_hash(bytes: bytearray,
                 algorithm,
                 key: int = CHROMATIC_SCALE,
                 note_duration: int = DEFAULT_NOTE_DURATION,
                 sample_rate: int = DEFAULT_SAMPLE_RATE) -> ndarray:
    hashed_bytes = algorithm(bytes).digest()
    pitches = bytes_to_pitches(hashed_bytes, key)
    return pitch_list_to_song(pitches, note_duration, sample_rate)

def musical_md5(bytes: bytearray,
                key: int = CHROMATIC_SCALE,
                note_duration: int = DEFAULT_NOTE_DURATION,
                sample_rate: int = DEFAULT_SAMPLE_RATE):
    return musical_hash(bytes, md5, key, note_duration, sample_rate)

def musical_sha1():
    pass

def musical_sha224():
    pass

def musical_sha384():
    pass

def musical_sha512():
    pass

def musical_blake2b():
    pass

def musical_blake2s():
    pass

def musical_crc32():
    pass
