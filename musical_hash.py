#/usr/bin/env python

import numpy
import scipy
import cv2
import wave
import struct
import wavio

from hashlib import md5, sha1
from numpy import append, empty, linspace, ndarray, sin
from typing import Callable, List

DEFAULT_SAMPLE_RATE = 44100
DEFAULT_NOTE_DURATION = 1
PITCH_STANDARD = 440
CHROMATIC_SCALE = 0xfff
E_MAJOR = 0xad5

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
    notes = numpy.zeros(12, note_duration * sample_rate)
    for tone in tones:
        note = numpy.zeros(note_duration * sample_rate)
        for harmonic in range(1,5):
            note = numpy.add(sin(2 * numpy.pi * tone * harmonic * linspace(0, note_duration, sample_rate)), note)
            
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
    
    


if __name__ == '__main__':
    message = "Hello World!"
    message_bits = []
    for byte in message:
        for i in range(8):
            message_bits.append((ord(byte) & (1 << (7 - i))) >> (7 - i))
    print(message_bits)
    filename = input('File?')
    img = cv2.imread(filename)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            for channel in range(min(img.shape[2], 3)):
                img[x][y][channel] = (img[x][y][channel] & 0xfe) + message_bits[x + y + channel]