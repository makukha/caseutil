from argparse import ArgumentParser
import sys

from . import __version__
from .cases import CASES, to_case, get_cases


parser = ArgumentParser(prog='caseutil', description=__doc__)
parser.add_argument('text', default=sys.stdin, nargs='?')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--version', action='version', version='%(prog)s ' + __version__)
group.add_argument('-c', '--convert', choices=CASES)
group.add_argument('-d', '--detect', action='store_true')


def main():
    args = parser.parse_args()

    if args.convert:
        for line in source_lines(args.text):
            print(to_case(args.convert, line))
    if args.detect:
        for line in source_lines(args.text):
            print(' '.join(get_cases(line)))


def source_lines(source):
    if hasattr(source, 'readline'):
        for line in source:
            yield line
    elif isinstance(source, str):
        for line in source.splitlines():
            yield line
    else:
        raise TypeError('Unsupported source type')


if __name__ == '__main__':
    main()
