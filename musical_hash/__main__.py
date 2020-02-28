"""Main docstring."""

from argparse import ArgumentParser
# from musical_hash import MusicalHash


def main():
    """Entry point for command-line execution."""
    parser = ArgumentParser(description='Return the musical hash of a string')
    parser.add_argument(
        'string',
        action='store',
        help='The string to hash')
    parser.add_argument(
        '--output_format',
        action='store',
        choices=['notes', 'wave', 'midi'],
        help='The output format',
        dest='output_format')
    parser.add_argument(
        '--key',
        action='store',
        help='The musical key of the output hash',
        dest='key')
    parser.add_argument(
        '--note_duration',
        action='store',
        type=float,
        help='The duration of each note in seconds',
        dest='note_duration')
    parser.add_argument(
        '--instrument',
        action='store',
        type=int,
        help='(Midi only) Selects the instrument to use in the output .midi '
             'file. Must be an integer. This may very depending on system.',
        dest='instrument')
    parser.parse_args()


if __name__ == '__main__':
    main()
