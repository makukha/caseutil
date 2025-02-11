from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
import textwrap

from . import __version__
from .cases import Case, to_case, get_cases


CASES = Case.as_tuple()


parser = ArgumentParser(
    prog='caseutil',
    formatter_class=RawDescriptionHelpFormatter,
    description=textwrap.dedent(
        """
        Convert, detect, or match text case.\n
        When stdin is used as input, each line is tokenized and processed separately.\n
        <case> choices:
          {}
        """.format(','.join(CASES))
    ),
)
help_text = 'text to be converted; if missing, stdin is used'
parser.add_argument('text', default=sys.stdin, nargs='?', help=help_text)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--version', action='version', version='%(prog)s ' + __version__)

help_c = 'convert [text] or stdin to <case>'
help_d = 'detect cases in [text] or stdin'
group.add_argument('-c', '--convert', choices=CASES, metavar='<case>', help=help_c)
group.add_argument('-d', '--detect', action='store_true', help=help_d)


def main():
    args = parser.parse_args()

    if args.convert:
        for line in source_lines(args.text):
            print(to_case(args.convert, line))
    elif args.detect:
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


if __name__ == '__main__':  # pragma: no cover
    main()
