import io
from subprocess import CalledProcessError, STDOUT, check_output
from unittest import TestCase

from unittest_expander import expand, foreach  # type: ignore

from caseutil import __main__, __version__
from caseutil.__main__ import ioable
from tests import data

# compatibility overrides

try:
    from typing_extensions import List, Optional, Tuple  # noqa: F401 # used in comments
except ImportError:
    pass


def assertErr(self, exc, msg):  # type: (TestCase, CalledProcessError, str) -> None
    self.assertNotEqual(exc.returncode, 0)
    out = exc.output if isinstance(exc.output, str) else exc.output.decode()
    self.assertIn(msg, out)


# tests


CASEUTIL = ['python', '-m', 'caseutil']


@expand
class CliHelpVersionInvalid(TestCase):
    def test_help(self):  # type: () -> None
        out = check_output(CASEUTIL + ['--help'])
        self.assertIn(b'usage: caseutil', out)

    def test_version(self):  # type: () -> None
        expected = 'caseutil {}\n'.format(__version__).encode()
        out = check_output(CASEUTIL + ['--version'], stderr=STDOUT)
        self.assertIn(expected, out)

    @foreach(
        'UnExPeCtEd',  # missing required option
        '--unexpected',  # unexpected option
    )  # type: ignore
    def test_invalid(self, arg):  # type: (str) -> None
        try:
            check_output(CASEUTIL + [arg], stderr=STDOUT)
        except CalledProcessError as err:
            assertErr(self, err, 'error: one of the arguments')


@expand()
class CliNormal(TestCase):
    def setUp(self):  # type: () -> None
        self.stdin = io.StringIO()
        self.stdout = io.StringIO()

    def call_cli(self, args):  # type: (List[str]) -> None
        __main__.cli(args, stdin=self.stdin, stdout=self.stdout)

    # convert

    @foreach(*data.X_MVN_OUT)  # type: ignore
    def test_convert_mvn(self, case, result):  # type: (str, str) -> None
        expected = '{}\n'.format(result)
        self.call_cli(['-c', case, data.X_MVN_IN])
        self.assertEqual(expected, self.stdout.getvalue())

    def test_convert_multiline(self):  # type: () -> None
        text = data.X_MVN_IN
        case = 'snake'
        conv = str([t for c, t in data.X_MVN_OUT if c == case][0])
        in_lines = ''.join('{}{}\n'.format(text, i) for i in range(3))
        expected = ''.join('{}{}\n'.format(conv, i) for i in range(3))
        self.stdin = io.StringIO(ioable(in_lines))
        self.call_cli(['-c', case])
        self.assertEqual(expected, self.stdout.getvalue())

    # detect

    @foreach(*data.X_MVN_OUT)  # type: ignore
    def test_detect_mvn(self, case, result):  # type: (str, str) -> None
        expected = '{}\n'.format(case)
        self.call_cli(['-d', result])
        self.assertEqual(expected, self.stdout.getvalue())

    @foreach(*data.X_AMBIGUOUS)  # type: ignore
    def test_detect_ambiguous(self, text, caselist):  # type: (str, str) -> None
        expected = '{}\n'.format(caselist)
        self.call_cli(['-d', text])
        self.assertEqual(expected, self.stdout.getvalue())

    def test_detect_mixed(self):  # type: () -> None
        self.call_cli(['-d', data.X_MIXED])
        self.assertEqual('\n', self.stdout.getvalue())
