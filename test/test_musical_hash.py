import musical_hash
import unittest


class TestConstructor(unittest.TestCase):
    """Test case for the MusicalHash constructor."""
    
    def setUp(self):
        self.dummy_function = lambda x : x

    def check_assertions(self, musical_hash_object, expectation):
        self.assertEqual(
            musical_hash_object.data,
            expectation['data'],
            'Data field copied correctly')
        self.assertEqual(
            musical_hash_object.hash_method,
            expectation['hash_method'],
            'Hash method copied correctly')
        self.assertEqual(
            musical_hash_object.hashed_bytes,
            expectation['hashed_bytes'],
            'Hashed bytes calculated correctly')

    def test_empty_bytearray(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', self.dummy_function),
            {
                'data': b'',
                'hash_method': self.dummy_function,
                'hashed_bytes': b''})

    def test_single_byte_bytearray(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'A', self.dummy_function),
            {
                'data': b'A',
                'hash_method': self.dummy_function,
                'hashed_bytes': b'A'})

    def test_multibyte_byte_array(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'AB', self.dummy_function),
            {
                'data': b'AB',
                'hash_method': self.dummy_function,
                'hashed_bytes': b'AB'})

    def test_md5(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'md5'),
            {
                'data': b'',
                'hash_method': 'md5',
                'hashed_bytes': b'\xd4\x1d\x8c\xd9\x8f\x00\xb2\x04\xe9\x80\t' \
                                b'\x98\xec\xf8B~'})

    def test_sha1(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha1'),
            {
                'data': b'',
                'hash_method': 'sha1',
                'hashed_bytes': b'\xda9\xa3\xee^kK\r2U\xbf\xef\x95`\x18\x90' \
                                b'\xaf\xd8\x07\t'})
    
    def test_sha224(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha224'),
            {
                'data': b'',
                'hash_method': 'sha224',
                'hashed_bytes': b'\xd1J\x02\x8c*:+\xc9Ga\x02\xbb(\x824\xc4' \
                                b'\x15\xa2\xb0\x1f\x82\x8e\xa6*\xc5\xb3\xe4/'})

    def test_sha384(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha384'),
            {
                'data': b'',
                'hash_method': 'sha384',
                'hashed_bytes': b"8\xb0`\xa7Q\xac\x968L\xd92~\xb1\xb1\xe3j!" \
                                b"\xfd\xb7\x11\x14\xbe\x07CL\x0c\xc7\xbfc" \
                                b"\xf6\xe1\xda'N\xde\xbf\xe7oe\xfb\xd5\x1a" \
                                b"\xd2\xf1H\x98\xb9["})

    def test_sha512(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'sha512'),
            {
                'data': b'',
                'hash_method': 'sha512',
                'hashed_bytes': b"\xcf\x83\xe15~\xef\xb8\xbd\xf1T(P\xd6m" \
                                b"\x80\x07\xd6 \xe4\x05\x0bW\x15\xdc\x83" \
                                b"\xf4\xa9!\xd3l\xe9\xceG\xd0\xd1<]\x85\xf2" \
                                b"\xb0\xff\x83\x18\xd2\x87~\xec/c\xb91\xbdGAz" \
                                b"\x81\xa582z\xf9'\xda>"})

    def test_blake2b(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'blake2b'),
            {
                'data': b'',
                'hash_method': 'blake2b',
                'hashed_bytes': b'xj\x02\xf7B\x01Y\x03\xc6\xc6\xfd\x85%R\xd2r' \
                                b'\x91/G@\xe1XGa\x8a\x86\xe2\x17\xf7\x1fT\x19' \
                                b'\xd2^\x101\xaf\xeeXS\x13\x89dD\x93N\xb0K' \
                                b'\x90:h[\x14H\xb7U\xd5op\x1a\xfe\x9b\xe2\xce'})

    def test_blake2s(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'blake2s'),
            {
                'data': b'',
                'hash_method': 'blake2s',
                'hashed_bytes': b'i!z0y\x90\x80\x94\xe1\x11!\xd0B5J|\x1fU' \
                                b'\xb6H,\xa1\xa5\x1e\x1b%\r\xfd\x1e\xd0\xee' \
                                b'\xf9'})

    def test_adler32(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'adler32'),
            {
                'data': b'',
                'hash_method': 'adler32',
                'hashed_bytes': b'\x01\x00\x00\x00'})

    def test_crc32(self):
        self.check_assertions(
            musical_hash.MusicalHash(b'', 'crc32'),
            {
                'data': b'',
                'hash_method': 'crc32',
                'hashed_bytes': b'\x00\x00\x00\x00'})


class TestGetScaleFrequencies(unittest.TestCase):
    """Test case for the _get_scale_frequencies method."""
    
    def setUp(self):
        self.hash = musical_hash.MusicalHash(b'', 'md5')

    def test_no_notes(self):
        self.assertEqual(
            self.hash._get_scale_frequencies(0x0),
            [],
            'No notes should be returned for an empty scale.')

    def test_one_note(self):
        self.assertEqual(
            self.hash._get_scale_frequencies(0x1),
            [musical_hash.PITCH_STANDARD],
            'Single note at pitch standard should be returned for 0x1.')

    def test_two_notes(self):
        self.assertEqual(
            self.hash._get_scale_frequencies(0xa),
            [
                musical_hash.PITCH_STANDARD * (2 ** (1/12)),
                musical_hash.PITCH_STANDARD * (2 ** (3/12))],
            'Two notes scale with no note at pitch standard.')

class TestPitchesToTune(unittest.TestCase):
    """Test case for the _pitches_to_tune method."""

    def setUp(self):
        self.hash = musical_hash.MusicalHash(b'', 'md5')

    def test_empty_pitch_list(self):
        pass

    def test_one_element_pitch_list(self):
        pass

    def test_multi_element_pitch_list(self):
        pass

    def test_negative_note_duration(self):
        pass

    def test_zero_note_duration(self):
        pass

    def test_positive_note_duration(self):
        pass

    def test_negative_sample_rate(self):
        pass

    def test_zero_sample_rate(self):
        pass

    def test_positive_sample_rate(self):
        pass


if __name__ == '__main__':
    unittest.main()