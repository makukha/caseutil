from unittest import TestCase

from doctestcase import doctestcase


@doctestcase()
class BasicUsage(TestCase):
    """
    Basic usage

    >>> from caseutil import is_snake, to_snake

    >>> is_snake('Foo bar-baz')
    False

    >>> to_snake('Foo bar-baz')
    'foo_bar_baz'
    """


@doctestcase()
class CasesEnum(TestCase):
    """
    Cases enum

    All supported cases are gathered in `Case` enum:

    ```python
    class Case(StrEnum):
        ADA = 'ada'
        CAMEL = 'camel'
        COBOL = 'cobol'
        CONST = 'const'
        KEBAB = 'kebab'
        LOWER = 'lower'
        PASCAL = 'pascal'
        SENTENCE = 'sentence'
        SNAKE = 'snake'
        TITLE = 'title'
        TRAIN = 'train'
        UPPER = 'upper'
    ```
    """


@doctestcase()
class ArbitraryCases(TestCase):
    """
    Arbitrary cases

    Use functions `is_case()` and `to_case()` to deal with arbitrary supported case:

    >>> from caseutil import Case, is_case, to_case

    >>> is_case(Case.CAMEL, 'myVarName')
    True

    >>> to_case(Case.CONST, 'myVarName')
    'MY_VAR_NAME'
    """


@doctestcase()
class DetectCases(TestCase):
    """
    Detect cases

    Use function `get_cases()` to determine case (or cases, if
    [ambiguous](https://caseutil.readthedocs.io/en/latest/classification/#ambiguity)):

    >>> from caseutil import get_cases

    >>> get_cases('fooBar')
    ('camel',)

    >>> get_cases('My var-name')  # mixed case
    ()

    >>> get_cases('Title')  # matches multiple cases
    ('ada', 'pascal', 'sentence', 'title', 'train')
    """


@doctestcase()
class CustomSeparators(TestCase):
    """
    Custom separators

    Use function `words()`:

    >>> from caseutil import words, to_lower

    >>> '/'.join(words(to_lower('myVarName')))
    'my/var/name'

    >>> '.'.join(words('myVarName'))
    'my.Var.Name'
    """


@doctestcase()
class Tokenization(TestCase):
    """
    Tokenization

    Word separators are non-word characters including underscore, and places where
    text case is changed from lower to upper. Digits are not treated as separators.
    For more details, see
    [Tokenization rules](https://caseutil.readthedocs.io/en/latest/tokenize).

    >>> from caseutil import words

    >>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
    ['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
    """


@doctestcase()
class UnicodeSupport(TestCase):
    """
    Unicode support *(not implemented)*

    Only ASCII names are supported. Unicode support is planned.
    """
