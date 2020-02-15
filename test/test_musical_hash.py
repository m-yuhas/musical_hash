import musical_hash
import unittest


class TestConstructor(unittest.TestCase):
    """Test case for the MusicalHash constructor."""

    def test_empty_bytearray(self):
        pass

class TestGetScaleFrequencies(unittest.TestCase):
    """Test case for the _get_scale_frequencies methods."""
    
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
        


if __name__ == '__main__':
    unittest.main()