from subprocess import CalledProcessError, STDOUT, check_output
from unittest import TestCase

from unittest_expander import expand, foreach  # type: ignore

from caseutil import __version__
from tests import data

# compatibility overrides

try:
    from typing_extensions import Tuple  # noqa: F401 # used in comments
except ImportError:
    pass


# helpers

def assertErr(self, exc, msg):  # type: (TestCase, CalledProcessError, str) -> None
    self.assertNotEqual(exc.returncode, 0)
    out = exc.output if isinstance(exc.output, str) else exc.output.decode()
    self.assertIn(msg, out)


# tests

@expand()
class TestCli(TestCase):
    def test_version(self):  # type: () -> None
        out = check_output(['python', '-m', 'caseutil', '--version'], stderr=STDOUT)
        self.assertEqual(b'caseutil ' + __version__.encode(), out.strip())

    @foreach(
        'UnExPeCtEd',  # missing required option
        '--unexpected',  # unexpected option
    )  # type: ignore
    def test_invalid_args(self, arg):  # type: (str) -> None
        try:
            check_output(['python', '-m', 'caseutil', arg], stderr=STDOUT)
        except CalledProcessError as e:
            assertErr(self, e, 'one of the arguments')
        else:
            self.fail('Expected CalledProcessError')

    # convert

    @foreach(*data.X_MVN_OUT)  # type: ignore
    def test_convert_mvn(self, case, result):  # type: (str, str) -> None
        expected = '{}\n'.format(result).encode()
        out = check_output(['python', '-m', 'caseutil', '-c', case, data.X_MVN_IN])
        self.assertEqual(expected, out)

    # def test_convert_multiline(self):  # type: () -> None
    #     text = data.INPUT_MVN
    #     case = 'snake'
    #     conv = str([t for c, t in data.OUTPUT_MVN if c == case][0])
    #     in_lines = ''.join('{}{}\n'.format(text, i) for i in range(3))
    #     expected = ''.join('{}{}\n'.format(conv, i) for i in range(3)).encode()
    #     cmd = 'echo "{}" | python -m caseutil -c {}'.format(in_lines, case)
    #     out = check_output(['sh', '-c', cmd])
    #     self.assertEqual(expected, out)

    # detect

    @foreach(*data.X_MVN_OUT)  # type: ignore
    def test_detect_mvn(self, case, result):  # type: (str, str) -> None
        expected = '{}\n'.format(case).encode()
        out = check_output(['python', '-m', 'caseutil', '-d', result])
        self.assertEqual(expected, out)

    @foreach(*data.X_AMBIGUOUS)  # type: ignore
    def test_detect_ambiguous(self, text, caselist):  # type: (str, str) -> None
        expected = '{}\n'.format(caselist).encode()
        out = check_output(['python', '-m', 'caseutil', '-d', text])
        self.assertEqual(expected, out)

    def test_detect_mixed(self):  # type: () -> None
        out = check_output(['python', '-m', 'caseutil', '-d', data.X_MIXED])
        self.assertEqual(b'\n', out)
