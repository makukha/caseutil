from itertools import product
from unittest import TestCase

from doctestcase import doctestcase
from unittest_expander import expand, foreach  # type: ignore

import caseutil
from caseutil import Case, get_cases, is_case, to_case
from tests import data

# compatibility overrides

try:
    from typing_extensions import Tuple  # noqa: F401 # used in comments
except ImportError:
    pass


@expand
@doctestcase()
class TestOperations(TestCase):
    """
    Invalid cases raise ValueError

    >>> from caseutil import is_case, to_case

    >>> is_case('unsupported', 'any text')
    Traceback (most recent call last):
        ...
    ValueError: Unsupported case: unsupported

    >>> to_case('unsupported', 'any text')
    Traceback (most recent call last):
        ...
    ValueError: Unsupported case: unsupported
    """
    def test_empty_string(self):  # type: () -> None
        all_cases = Case.as_tuple()
        self.assertFalse(any(is_case(c, '') for c in all_cases))
        self.assertTrue(all(to_case(c, '') == '' for c in all_cases))

    def test_mixed(self):  # type: () -> None
        text = data.X_MIXED
        all_cases = Case.as_tuple()
        # detect universal
        self.assertFalse(any(is_case(c, text) for c in all_cases))
        # get cases
        self.assertEqual((), get_cases(text))

    @foreach(*data.X_MVN_OUT)  # type: ignore
    def test_mvn(self, case, expected):  # type: (str, str) -> None
        text = data.X_MVN_IN
        # convert
        convert = getattr(caseutil, 'to_' + case)
        self.assertEqual(expected, convert(text))
        self.assertEqual(expected, to_case(case, text))
        # detect specific
        detect = getattr(caseutil, 'is_' + case)
        self.assertFalse(detect(text))
        self.assertTrue(detect(expected))
        # detect arbitrary
        self.assertFalse(is_case(case, text))
        self.assertTrue(is_case(case, expected))
        # get cases
        self.assertEqual((case,), get_cases(expected))

    @foreach(*data.X_AMBIGUOUS)  # type: ignore
    def test_ambiguous(self, text, caselist):  # type: (str, str) -> None
        all_cases = Case.as_tuple()
        cases = tuple(caselist.split())
        other_cases = tuple(c for c in all_cases if c not in cases)
        # detect
        self.assertTrue(all(is_case(c, text) for c in cases))
        self.assertFalse(any(is_case(c, text) for c in other_cases))
        # get cases
        self.assertEqual(cases, get_cases(text))

    def test_cross_check(self):  # type: () -> None
        text = data.X_MIXED
        all_cases = Case.as_tuple()
        for c1, c2 in product(all_cases, repeat=2):
            self.assertEqual(c1 == c2, is_case(c1, to_case(c2, text)))
