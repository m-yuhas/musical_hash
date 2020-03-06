"""Unit test cases for the _musical_hash module."""


from typing import Callable, Dict, List, Union
import os
import unittest
import mido
import numpy
import wavio
import musical_hash


Expectation = Dict[str,
                   Union[int,
                         float,
                         bytearray,
                         str,
                         List[float],
                         Callable[[bytearray], bytearray]]]


class TestConstructor(unittest.TestCase):
    """Test case for the MusicalHash constructor."""

    def setUp(self) -> None:
        """Create a dummy function for testing the constructor."""
        self.dummy_function = lambda x: x

    def check_assertions(self,
                         musical_hash_object: musical_hash.MusicalHash,
                         expectation: Expectation) -> None:
        """Simplify assertion checks for constructor tests."""
        self.assertEqual(
            musical_hash_object.data,
            expectation['data'],
            'Data field not copied correctly')
        self.assertEqual(
            musical_hash_object.hash_method,
            expectation['hash_method'],
            'Hash method not copied correctly')
        self.assertEqual(
            musical_hash_object.hashed_bytes,
            expectation['hashed_bytes'],
            'Hashed bytes not calculated correctly')

    def test_empty_bytearray(self) -> None:
        """Test constructor when the bytearray is empty."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', self.dummy_function),
            {
                'data': b'',
                'hash_method': self.dummy_function,
                'hashed_bytes': b''})

    def test_single_byte_bytearray(self) -> None:
        """Test constructor when a single byte is input as the bytearray."""
        self.check_assertions(
            musical_hash.MusicalHash(b'A', self.dummy_function),
            {
                'data': b'A',
                'hash_method': self.dummy_function,
                'hashed_bytes': b'A'})

    def test_multibyte_byte_array(self) -> None:
        """Test constructor when multiple bytes are input as the bytearray."""
        self.check_assertions(
            musical_hash.MusicalHash(b'AB', self.dummy_function),
            {
                'data': b'AB',
                'hash_method': self.dummy_function,
                'hashed_bytes': b'AB'})

    def test_md5(self) -> None:
        """Test constructor with md5 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'md5'),
            {
                'data': b'',
                'hash_method': 'md5',
                'hashed_bytes': b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t'
                                b'\x98\xec\xf8B~'})

    def test_sha1(self) -> None:
        """Test constructor with sha1 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha1'),
            {
                'data': b'',
                'hash_method': 'sha1',
                'hashed_bytes': b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90'
                                b'\xaf\xd8\x07\t'})

    def test_sha224(self) -> None:
        """Test constructor with sha224 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha224'),
            {
                'data': b'',
                'hash_method': 'sha224',
                'hashed_bytes': b'\xd1J\x02\x8c*:+\xc9Ga\x02\xbb(\x824\xc4'
                                b'\x15\xa2\xb0\x1f\x82\x8e\xa6*\xc5\xb3\xe4/'})

    def test_sha384(self) -> None:
        """Test constructor with sha384 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha384'),
            {
                'data': b'',
                'hash_method': 'sha384',
                'hashed_bytes': b"8\xb0`\xa7Q\xac\x968L\xd92~\xb1\xb1\xe3j!"
                                b"\xfd\xb7\x11\x14\xbe\x07CL\x0c\xc7\xbfc"
                                b"\xf6\xe1\xda'N\xde\xbf\xe7oe\xfb\xd5\x1a"
                                b"\xd2\xf1H\x98\xb9["})

    def test_sha512(self) -> None:
        """Test constructor with sha512 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha512'),
            {
                'data': b'',
                'hash_method': 'sha512',
                'hashed_bytes': b"\xcf\x83\xe15~\xef\xb8\xbd\xf1T(P\xd6m"
                                b"\x80\x07\xd6 \xe4\x05\x0bW\x15\xdc\x83"
                                b"\xf4\xa9!\xd3l\xe9\xceG\xd0\xd1<]\x85\xf2"
                                b"\xb0\xff\x83\x18\xd2\x87~\xec/c\xb91\xbdGAz"
                                b"\x81\xa582z\xf9'\xda>"})

    def test_blake2b(self) -> None:
        """Test constructor with blake2b as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'blake2b'),
            {
                'data': b'',
                'hash_method': 'blake2b',
                'hashed_bytes': b'xj\x02\xf7B\x01Y\x03\xc6\xc6\xfd\x85%R\xd2r'
                                b'\x91/G@\xe1XGa\x8a\x86\xe2\x17\xf7\x1fT\x19'
                                b'\xd2^\x101\xaf\xeeXS\x13\x89dD\x93N\xb0K'
                                b'\x90:h[\x14H\xb7U\xd5op\x1a\xfe\x9b\xe2'
                                b'\xce'})

    def test_blake2s(self) -> None:
        """Test constructor with blake2s as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'blake2s'),
            {
                'data': b'',
                'hash_method': 'blake2s',
                'hashed_bytes': b'i!z0y\x90\x80\x94\xe1\x11!\xd0B5J|\x1fU'
                                b'\xb6H,\xa1\xa5\x1e\x1b%\r\xfd\x1e\xd0\xee'
                                b'\xf9'})

    def test_adler32(self) -> None:
        """Test constructor with adler32 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'adler32'),
            {
                'data': b'',
                'hash_method': 'adler32',
                'hashed_bytes': b'\x01\x00\x00\x00'})

    def test_crc32(self) -> None:
        """Test constructor with crc32 as hash type."""
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'crc32'),
            {
                'data': b'',
                'hash_method': 'crc32',
                'hashed_bytes': b'\x00\x00\x00\x00'})


class TestNotes(unittest.TestCase):
    """Test the notes method of the MusicalHash class."""

    def setUp(self) -> None:
        """Create a musical hash object for all tests in this case."""
        self.hash = musical_hash.MusicalHash(b'Hello World', 'md5')

    def test_defaults(self) -> None:
        """Test default arguments."""
        self.assertEqual(
            self.hash.notes(),
            ['#A', '#C', '#C', 'C', '#C', '#C', 'A', '#D', 'F', 'C', 'F', 'B',
             '#G', 'A', '#A', '#C', '#F', 'E', 'G', '#C', 'A', 'G', 'C', 'B',
             'E', '#A', 'F', 'D', 'G', 'D', 'D', 'E', 'G', 'G', '#A', 'D'],
            'Representation as notes not correct')

    def test_no_notes_in_key(self) -> None:
        """Test with a key with no notes."""
        with self.assertRaises(ValueError):
            self.hash.notes(key=0x0)

    def test_one_note_in_key(self) -> None:
        """Test with a key with one note."""
        with self.assertRaises(ValueError):
            self.hash.notes(key=0x1)

    def test_two_notes_in_key(self) -> None:
        """Test with a key with two notes."""
        self.assertEqual(
            self.hash.notes(key=0x5),
            ['B', 'A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A',
             'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'B', 'A',
             'A', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'B', 'B',
             'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'B', 'A',
             'B', 'B', 'B', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'A', 'B',
             'A', 'B', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'B',
             'A', 'B', 'B', 'A', 'A', 'B', 'A', 'B', 'A', 'B', 'B', 'B', 'A',
             'B', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'A', 'A', 'B', 'B', 'B',
             'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'B', 'B',
             'B', 'A', 'A', 'B', 'A', 'B', 'A', 'A', 'B', 'B', 'B'],
            'Representation as notes not correct')

    def test_too_many_notes_in_key(self) -> None:
        """Test key with too many notes."""
        with self.assertRaises(ValueError):
            self.hash.notes(key=0x1fff)

    def test_flats(self) -> None:
        """Test with flats selected instead of sharps."""
        self.assertEqual(
            self.hash.notes(key=musical_hash.CHROMATIC_SCALE, sharps=False),
            ['bB', 'bD', 'bD', 'C', 'bD', 'bD', 'A', 'Eb', 'F', 'C', 'F', 'B',
             'bA', 'A', 'bB', 'bD', 'bG', 'E', 'G', 'bD', 'A', 'G', 'C', 'B',
             'E', 'bB', 'F', 'D', 'G', 'D', 'D', 'E', 'G', 'G', 'bB', 'D'],
            'Representation as notes not correct')


class TestSamples(unittest.TestCase):
    """Test the samples method of the MusicalHash class."""

    def setUp(self) -> None:
        """Construct a MusicalHash object for this test."""
        self.hash = musical_hash.MusicalHash(b'Hello World', 'md5')

    def check_assertions(self,
                         key: int,
                         note_duration: float,
                         sample_rate: int,
                         expected_notes: List[float]) -> None:
        """Simplify assertion checks for samples method."""
        samples = self.hash.samples(key, note_duration, sample_rate)
        self.assertEqual(
            samples.size,
            len(expected_notes) * int(note_duration * sample_rate),
            'Output tune is not the correct length.')
        for note, frequency in enumerate(expected_notes):
            spectrum = numpy.fft.fft(
                samples[note * int(
                    sample_rate * note_duration):(
                        note + 1) * int(sample_rate * note_duration)])
            spectral_density = 10 * numpy.log10(
                numpy.absolute(numpy.square(spectrum[:int(spectrum.size/2)])))
            self.assertGreater(
                spectral_density[int(frequency * note_duration)],
                numpy.average(spectral_density),
                'Output pitch is not present within the expected interval.')

    def test_no_notes_in_key(self) -> None:
        """Test with a key with no notes."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x0)

    def test_one_note_in_key(self) -> None:
        """Test with a key with one note."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x2)

    def test_two_notes_in_key(self) -> None:
        """Test with a scale with two notes."""
        self.check_assertions(
            key=0x5,
            note_duration=0.5,
            sample_rate=44100,
            expected_notes=[466.1637615180899, 440.0, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899, 440.0,
                            466.1637615180899, 440.0, 466.1637615180899, 440.0,
                            466.1637615180899, 440.0, 440.0, 440.0, 440.0,
                            466.1637615180899, 440.0, 466.1637615180899,
                            466.1637615180899, 440.0, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899,
                            440.0, 440.0, 440.0, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899,
                            440.0, 440.0, 466.1637615180899, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899, 440.0, 440.0,
                            440.0, 440.0, 440.0, 440.0, 466.1637615180899,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899,
                            440.0, 466.1637615180899, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899, 440.0,
                            440.0, 440.0, 440.0, 440.0, 466.1637615180899,
                            440.0, 466.1637615180899, 440.0, 466.1637615180899,
                            440.0, 440.0, 440.0, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899,
                            466.1637615180899, 440.0, 440.0, 466.1637615180899,
                            440.0, 466.1637615180899, 440.0, 466.1637615180899,
                            466.1637615180899, 466.1637615180899, 440.0,
                            466.1637615180899, 466.1637615180899, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 466.1637615180899, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 440.0, 466.1637615180899,
                            466.1637615180899, 466.1637615180899, 440.0,
                            466.1637615180899, 440.0, 440.0, 466.1637615180899,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899, 440.0, 440.0, 466.1637615180899,
                            440.0, 466.1637615180899, 440.0, 440.0,
                            466.1637615180899, 466.1637615180899,
                            466.1637615180899])

    def test_chromatic_scale(self):
        """Test with a chromatic scale."""
        self.check_assertions(
            key=0xfff,
            note_duration=0.5,
            sample_rate=44100,
            expected_notes=[466.1637615180899, 554.3652619537442,
                            554.3652619537442, 523.2511306011972,
                            554.3652619537442, 554.3652619537442,
                            440.0, 622.2539674441618, 698.4564628660078,
                            523.2511306011972, 698.4564628660078,
                            493.8833012561241, 830.6093951598903, 440.0,
                            466.1637615180899, 554.3652619537442,
                            739.9888454232688, 659.2551138257398,
                            783.9908719634985, 554.3652619537442, 440.0,
                            783.9908719634985, 554.3652619537442,
                            493.8833012561241, 659.2551138257398,
                            466.1637615180899, 698.4564628660078,
                            587.3295358348151, 783.9908719634985,
                            587.3295358348151, 587.3295358348151,
                            659.2551138257398, 783.9908719634985,
                            783.9908719634985, 466.1637615180899,
                            587.3295358348151])

    def test_too_many_notes_in_key(self) -> None:
        """Test key with too many notes."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x2fff)

    def test_negative_note_duration(self) -> None:
        """Test negative note duration."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x111, note_duration=-1)

    def test_zero_note_duration(self) -> None:
        """Test zero note duration."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x111, note_duration=0)

    def test_positive_note_duration(self) -> None:
        """Test positive note duration."""
        self.check_assertions(
            key=0xfff,
            note_duration=1,
            sample_rate=44100,
            expected_notes=[466.1637615180899, 554.3652619537442,
                            554.3652619537442, 523.2511306011972,
                            554.3652619537442, 554.3652619537442,
                            440.0, 622.2539674441618, 698.4564628660078,
                            523.2511306011972, 698.4564628660078,
                            493.8833012561241, 830.6093951598903, 440.0,
                            466.1637615180899, 554.3652619537442,
                            739.9888454232688, 659.2551138257398,
                            783.9908719634985, 554.3652619537442, 440.0,
                            783.9908719634985, 554.3652619537442,
                            493.8833012561241, 659.2551138257398,
                            466.1637615180899, 698.4564628660078,
                            587.3295358348151, 783.9908719634985,
                            587.3295358348151, 587.3295358348151,
                            659.2551138257398, 783.9908719634985,
                            783.9908719634985, 466.1637615180899,
                            587.3295358348151])

    def test_negative_sample_rate(self) -> None:
        """Test negative sample rate."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x111, note_duration=1, sample_rate=-44100)

    def test_zero_sample_rate(self) -> None:
        """Test zero sample rate."""
        with self.assertRaises(ValueError):
            self.hash.samples(key=0x111, note_duration=1, sample_rate=0)

    def test_positive_sample_rate(self) -> None:
        """Test positive sample rate."""
        self.check_assertions(
            key=0xfff,
            note_duration=1,
            sample_rate=96000,
            expected_notes=[466.1637615180899, 554.3652619537442,
                            554.3652619537442, 523.2511306011972,
                            554.3652619537442, 554.3652619537442,
                            440.0, 622.2539674441618, 698.4564628660078,
                            523.2511306011972, 698.4564628660078,
                            493.8833012561241, 830.6093951598903, 440.0,
                            466.1637615180899, 554.3652619537442,
                            739.9888454232688, 659.2551138257398,
                            783.9908719634985, 554.3652619537442, 440.0,
                            783.9908719634985, 554.3652619537442,
                            493.8833012561241, 659.2551138257398,
                            466.1637615180899, 698.4564628660078,
                            587.3295358348151, 783.9908719634985,
                            587.3295358348151, 587.3295358348151,
                            659.2551138257398, 783.9908719634985,
                            783.9908719634985, 466.1637615180899,
                            587.3295358348151])


class TestWave(unittest.TestCase):
    """Test the wave method of the MusicalHash class."""

    def setUp(self) -> None:
        """Construct a MusicalHash object for this test."""
        self.hash = musical_hash.MusicalHash(b'Hello World', 'md5')

    def check_assertions(self, expectation: Expectation) -> None:
        """Simplify assertion checks for wave method."""
        self.hash.wave(
            filename=expectation['filename'],
            key=expectation['key'],
            note_duration=expectation['note_duration'],
            sample_rate=expectation['sample_rate'])
        self.assertTrue(
            os.path.isfile(expectation['filename']), 'File not created.')
        wave_file = wavio.read(expectation['filename'])
        self.assertEqual(
            wave_file.rate,
            expectation['sample_rate'],
            'Sample rate of wave file does not match input rate.')
        self.assertEqual(
            len(wave_file.data),
            len(expectation['notes']) * int(
                expectation['note_duration'] * expectation['sample_rate']),
            'Output tune is not the correct length.')
        samples = numpy.squeeze(wave_file.data)
        for note, frequency in enumerate(expectation['notes']):
            spectrum = numpy.fft.fft(
                samples[note * int(
                    expectation['sample_rate'] *
                    expectation['note_duration']):(
                        note + 1) * int(
                            expectation['sample_rate'] *
                            expectation['note_duration'])])
            spectral_density = 10 * numpy.log10(
                numpy.absolute(numpy.square(spectrum[:int(spectrum.size/2)])))
            self.assertGreater(
                spectral_density[int(
                    frequency * expectation['note_duration'])],
                numpy.average(spectral_density),
                'Output pitch is not present within the expected interval.')

    def test_empty_filename(self) -> None:
        """Test with an empty filename."""
        with self.assertRaises(FileNotFoundError):
            self.hash.wave('')

    def test_unicode_filename(self) -> None:
        """Test with a unicode filename."""
        self.check_assertions({
            'filename': '散列.wav',
            'key': musical_hash.CHROMATIC_SCALE,
            'note_duration': 0.5,
            'sample_rate': 44100,
            'notes': [466.1637615180899, 554.3652619537442,
                      554.3652619537442, 523.2511306011972,
                      554.3652619537442, 554.3652619537442,
                      440.0, 622.2539674441618, 698.4564628660078,
                      523.2511306011972, 698.4564628660078,
                      493.8833012561241, 830.6093951598903, 440.0,
                      466.1637615180899, 554.3652619537442,
                      739.9888454232688, 659.2551138257398,
                      783.9908719634985, 554.3652619537442, 440.0,
                      783.9908719634985, 554.3652619537442,
                      493.8833012561241, 659.2551138257398,
                      466.1637615180899, 698.4564628660078,
                      587.3295358348151, 783.9908719634985,
                      587.3295358348151, 587.3295358348151,
                      659.2551138257398, 783.9908719634985,
                      783.9908719634985, 466.1637615180899,
                      587.3295358348151]})

    def test_unicode_filename2(self) -> None:
        """Test another unicode filename."""
        self.check_assertions({
            'filename': '🍎🍐🍊🍌.wav',
            'key': musical_hash.CHROMATIC_SCALE,
            'note_duration': 0.5,
            'sample_rate': 44100,
            'notes': [466.1637615180899, 554.3652619537442,
                      554.3652619537442, 523.2511306011972,
                      554.3652619537442, 554.3652619537442,
                      440.0, 622.2539674441618, 698.4564628660078,
                      523.2511306011972, 698.4564628660078,
                      493.8833012561241, 830.6093951598903, 440.0,
                      466.1637615180899, 554.3652619537442,
                      739.9888454232688, 659.2551138257398,
                      783.9908719634985, 554.3652619537442, 440.0,
                      783.9908719634985, 554.3652619537442,
                      493.8833012561241, 659.2551138257398,
                      466.1637615180899, 698.4564628660078,
                      587.3295358348151, 783.9908719634985,
                      587.3295358348151, 587.3295358348151,
                      659.2551138257398, 783.9908719634985,
                      783.9908719634985, 466.1637615180899,
                      587.3295358348151]})

    def test_no_notes_in_key(self) -> None:
        """Test with a key with no notes."""
        with self.assertRaises(ValueError):
            self.hash.wave('hash.wav', key=0x0)

    def test_one_note_in_key(self) -> None:
        """Test with a key with one note."""
        with self.assertRaises(ValueError):
            self.hash.wave('hash.wav', key=0x2)

    def test_two_notes_in_key(self) -> None:
        """Test with a scale with two notes."""
        self.check_assertions({
            'filename': 'test.wav',
            'key': 0x5,
            'note_duration': 0.5,
            'sample_rate': 44100,
            'notes': [466.1637615180899, 440.0, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899, 440.0,
                      466.1637615180899, 440.0, 466.1637615180899, 440.0,
                      466.1637615180899, 440.0, 440.0, 440.0, 440.0,
                      466.1637615180899, 440.0, 466.1637615180899,
                      466.1637615180899, 440.0, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899,
                      440.0, 440.0, 440.0, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899,
                      440.0, 440.0, 466.1637615180899, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899, 440.0, 440.0,
                      440.0, 440.0, 440.0, 440.0, 466.1637615180899,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899,
                      440.0, 466.1637615180899, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899, 440.0,
                      440.0, 440.0, 440.0, 440.0, 466.1637615180899,
                      440.0, 466.1637615180899, 440.0, 466.1637615180899,
                      440.0, 440.0, 440.0, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899,
                      466.1637615180899, 440.0, 440.0, 466.1637615180899,
                      440.0, 466.1637615180899, 440.0, 466.1637615180899,
                      466.1637615180899, 466.1637615180899, 440.0,
                      466.1637615180899, 466.1637615180899, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 466.1637615180899, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 440.0, 466.1637615180899,
                      466.1637615180899, 466.1637615180899, 440.0,
                      466.1637615180899, 440.0, 440.0, 466.1637615180899,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899, 440.0, 440.0, 466.1637615180899,
                      440.0, 466.1637615180899, 440.0, 440.0,
                      466.1637615180899, 466.1637615180899,
                      466.1637615180899]})

    def test_chromatic_scale(self):
        """Test with a chromatic scale."""
        self.check_assertions({
            'filename': 'test.wav',
            'key': 0xfff,
            'note_duration': 0.5,
            'sample_rate': 44100,
            'notes': [466.1637615180899, 554.3652619537442,
                      554.3652619537442, 523.2511306011972,
                      554.3652619537442, 554.3652619537442,
                      440.0, 622.2539674441618, 698.4564628660078,
                      523.2511306011972, 698.4564628660078,
                      493.8833012561241, 830.6093951598903, 440.0,
                      466.1637615180899, 554.3652619537442,
                      739.9888454232688, 659.2551138257398,
                      783.9908719634985, 554.3652619537442, 440.0,
                      783.9908719634985, 554.3652619537442,
                      493.8833012561241, 659.2551138257398,
                      466.1637615180899, 698.4564628660078,
                      587.3295358348151, 783.9908719634985,
                      587.3295358348151, 587.3295358348151,
                      659.2551138257398, 783.9908719634985,
                      783.9908719634985, 466.1637615180899,
                      587.3295358348151]})

    def test_too_many_notes_in_key(self) -> None:
        """Test key with too many notes."""
        with self.assertRaises(ValueError):
            self.hash.wave('test.wav', key=0x2fff)

    def test_negative_note_duration(self) -> None:
        """Test negative note duration."""
        with self.assertRaises(ValueError):
            self.hash.wave('test.wav', key=0x111, note_duration=-1)

    def test_zero_note_duration(self) -> None:
        """Test zero note duration."""
        with self.assertRaises(ValueError):
            self.hash.wave('test.wav', key=0x111, note_duration=0)

    def test_positive_note_duration(self) -> None:
        """Test positive note duration."""
        self.check_assertions({
            'filename': 'test.wav',
            'key': 0xfff,
            'note_duration': 1,
            'sample_rate': 44100,
            'notes': [466.1637615180899, 554.3652619537442,
                      554.3652619537442, 523.2511306011972,
                      554.3652619537442, 554.3652619537442,
                      440.0, 622.2539674441618, 698.4564628660078,
                      523.2511306011972, 698.4564628660078,
                      493.8833012561241, 830.6093951598903, 440.0,
                      466.1637615180899, 554.3652619537442,
                      739.9888454232688, 659.2551138257398,
                      783.9908719634985, 554.3652619537442, 440.0,
                      783.9908719634985, 554.3652619537442,
                      493.8833012561241, 659.2551138257398,
                      466.1637615180899, 698.4564628660078,
                      587.3295358348151, 783.9908719634985,
                      587.3295358348151, 587.3295358348151,
                      659.2551138257398, 783.9908719634985,
                      783.9908719634985, 466.1637615180899,
                      587.3295358348151]})

    def test_negative_sample_rate(self) -> None:
        """Test negative sample rate."""
        with self.assertRaises(ValueError):
            self.hash.wave(
                'test.wav',
                key=0x111,
                note_duration=1,
                sample_rate=-44100)

    def test_zero_sample_rate(self) -> None:
        """Test zero sample rate."""
        with self.assertRaises(ValueError):
            self.hash.wave(
                'test.wav',
                key=0x111,
                note_duration=1,
                sample_rate=0)

    def test_positive_sample_rate(self) -> None:
        """Test positive sample rate."""
        self.check_assertions({
            'filename': 'test.wav',
            'key': 0xfff,
            'note_duration': 1,
            'sample_rate': 96000,
            'notes': [466.1637615180899, 554.3652619537442,
                      554.3652619537442, 523.2511306011972,
                      554.3652619537442, 554.3652619537442,
                      440.0, 622.2539674441618, 698.4564628660078,
                      523.2511306011972, 698.4564628660078,
                      493.8833012561241, 830.6093951598903, 440.0,
                      466.1637615180899, 554.3652619537442,
                      739.9888454232688, 659.2551138257398,
                      783.9908719634985, 554.3652619537442, 440.0,
                      783.9908719634985, 554.3652619537442,
                      493.8833012561241, 659.2551138257398,
                      466.1637615180899, 698.4564628660078,
                      587.3295358348151, 783.9908719634985,
                      587.3295358348151, 587.3295358348151,
                      659.2551138257398, 783.9908719634985,
                      783.9908719634985, 466.1637615180899,
                      587.3295358348151]})

    def tearDown(self) -> None:
        """Clean up any created files."""
        for file in os.listdir():
            if file.endswith('.wav') and os.path.isfile(file):
                try:
                    os.remove(file)
                except OSError:
                    pass


class TestMidi(unittest.TestCase):
    """Test the midi method of the MusicalHash class."""

    def setUp(self) -> None:
        """Construct a MusicalHash object for this test."""
        self.hash = musical_hash.MusicalHash(b'Hello World', 'md5')

    def test_empty_filename(self) -> None:
        """Test with an empty filename."""
        with self.assertRaises(FileNotFoundError):
            self.hash.midi('')

    def test_unicode_filename(self) -> None:
        """Test with a unicode filename."""
        self.hash.midi('散列.mid')
        self.assertTrue(os.path.isfile('散列.mid'), 'File not created.')

    def test_unicode_filename2(self) -> None:
        """Test another unicode filename."""
        self.hash.midi('🍎🍐🍊🍌.mid')
        self.assertTrue(os.path.isfile('🍎🍐🍊🍌.mid'), 'File not created.')

    def test_no_notes_in_key(self) -> None:
        """Test with a key with no notes."""
        with self.assertRaises(ValueError):
            self.hash.midi('test.mid', key=0x0)

    def test_one_note_in_key(self) -> None:
        """Test with a key with one note."""
        with self.assertRaises(ValueError):
            self.hash.midi('test.mid', key=0x4)

    def test_two_notes_in_key(self) -> None:
        """Test with a scale with two notes."""
        self.hash.midi('test.mid', key=0xa)
        midi_file = mido.MidiFile('test.mid')
        notes_present = []
        for track in midi_file.tracks:
            for message in track:
                if (message.type == 'note_on' and
                        message.note not in notes_present):
                    notes_present.append(message.note)
        notes_present.sort()
        self.assertEqual(
            notes_present,
            [70, 72],
            'Incorrect notes in output midi file.')

    def test_chromatic_scale(self):
        """Test with a chromatic scale."""
        self.hash.midi('test.mid', key=0xfff)
        midi_file = mido.MidiFile('test.mid')
        notes_present = []
        for track in midi_file.tracks:
            for message in track:
                if (message.type == 'note_on' and
                        message.note not in notes_present):
                    notes_present.append(message.note)
        notes_present.sort()
        self.assertEqual(
            notes_present,
            [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
            'Incorrect notes in output midi file.')

    def test_too_many_notes_in_key(self) -> None:
        """Test key with too many notes."""
        with self.assertRaises(ValueError):
            self.hash.midi('test.mid', key=0x3fff)

    def test_negative_note_duration(self) -> None:
        """Test negative note duration."""
        with self.assertRaises(ValueError):
            self.hash.midi('test.mid', key=0x111, note_duration=-1)

    def test_zero_note_duration(self) -> None:
        """Test zero note duration."""
        with self.assertRaises(ValueError):
            self.hash.midi('test.mid', key=0x111, note_duration=0)

    def test_instrument_change(self) -> None:
        """Test changes to the selected midi instrument."""
        self.hash.midi('test.mid', instrument=0xa)
        midi_file = mido.MidiFile('test.mid')
        for i, track in enumerate(midi_file.tracks):
            self.assertEqual(
                track[0].type,
                'program_change',
                'Midi instrument needs to be set before playing notes.')
            if track[0].type == 'program_change':
                self.assertEqual(
                    track[0].program,
                    0xa,
                    'Incorrect instrument selected on track {}'.format(i))

    def tearDown(self) -> None:
        """Clean up any created files."""
        for file in os.listdir():
            if file.endswith('.mid') and os.path.isfile(file):
                try:
                    os.remove(file)
                except OSError:
                    pass


if __name__ == '__main__':
    unittest.main()
