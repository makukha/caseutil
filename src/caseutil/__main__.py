import io
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
import textwrap

from . import __version__
from .cases import Case, to_case, get_cases


# helpers


def stream(item):
    if isinstance(item, str):
        return io.StringIO(ioable(item if item.endswith('\n') else item + '\n'))
    return item


def ioable(value, encoding='utf-8'):
    if sys.version_info < (3,):  # pragma: nocover  # coverage runs on Python 3
        return value.decode(encoding)
    else:
        return value


# parser


parser = ArgumentParser(
    prog='caseutil',
    formatter_class=RawDescriptionHelpFormatter,
    description=textwrap.dedent(
        """
        Convert, detect, or match text case.\n
        When stdin is used as input, each line is tokenized and processed separately.\n
        <case> choices:
          {}
        """.format(','.join(Case.as_tuple()))
    ),
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--version', action='version', version='%(prog)s ' + __version__)

group.add_argument(
    '-c',
    '--convert',
    choices=Case.as_tuple(),
    metavar='<case>',
    help='convert [text] or stdin to <case>',
)
group.add_argument(
    '-d',
    '--detect',
    action='store_true',
    help='detect cases in [text] or stdin',
)
parser.add_argument(
    'text',
    nargs='?',
    help='text to be converted; if missing, stdin is used',
)


# entrypoint


def cli(argv=None, stdin=sys.stdin, stdout=sys.stdout):
    args = parser.parse_args(argv)
    if args.text is None:
        args.text = stdin

    def line(text):  # type: (str) -> str
        return ioable(text + '\n')

    if args.detect:
        stdout.writelines(line(' '.join(get_cases(ln))) for ln in stream(args.text))
    else:
        stdout.writelines(line(to_case(args.convert, ln)) for ln in stream(args.text))


if __name__ == '__main__':
    sys.exit(cli())
