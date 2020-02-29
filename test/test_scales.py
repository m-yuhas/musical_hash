"""Unit test cases for the _scales module."""


import unittest
import musical_hash


class TestGetScale(unittest.TestCase):
    """Test case for the get_scale function."""

    def test_empty_list(self) -> None:
        """Test when the input list is empty."""
        self.assertEqual(
            musical_hash.get_scale([]),
            0x0,
            'Scale should have no notes.')

    def test_one_note(self) -> None:
        """Test when the input list has one element."""
        self.assertEqual(
            musical_hash.get_scale(['A']),
            0x1,
            'Scale should only have an A')

    def test_twelve_notes(self) -> None:
        """Test when the input list has twelve elements."""
        self.assertEqual(
            musical_hash.get_scale(['A', '#A', 'B', 'C', '#C', 'D', '#D', 'E',
                                    'F', '#F', 'G', '#G']),
            0xfff,
            'Scale should contain all notes.')

    def test_duplicate_notes(self) -> None:
        """Test when the input list has duplicate notes."""
        self.assertEqual(
            musical_hash.get_scale(['A', '#A', 'bB', 'C', 'C']),
            0x00b,
            'Duplicate notes should be handled.')

    def test_invalid_notes(self) -> None:
        """Test when the input list contains invalid notes."""
        with self.assertRaises(ValueError):
            musical_hash.get_scale(['A', 'Foo', 'Bar'])


if __name__ == '__main__':
    unittest.main()
