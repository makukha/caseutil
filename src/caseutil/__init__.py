"""
Case convert and verify for Python: snake_case, camelCase, kebab-case, and more.
"""

from argparse import ArgumentParser
from io import TextIOBase
import re
import sys
from typing import List, Union

from .__version__ import __version__

__all__ = [
    'is_camel',
    'is_const',
    'is_kebab',
    'is_lower',
    'is_pascal',
    'is_snake',
    'is_title',
    'is_upper',
    'to_camel',
    'to_const',
    'to_kebab',
    'to_lower',
    'to_pascal',
    'to_snake',
    'to_title',
    'to_upper',
    # universal
    'Case',
    'is_case',
    'to_case',
    'words',
]


if sys.version_info.major == 2:  # pragma: no cover

    class _Case:  # pragma: no cover
        pass  # pragma: no cover
else:
    from enum import Enum

    class _Case(str, Enum):  # type: ignore[no-redef]
        pass


class Case(_Case):
    CAMEL = 'camel'
    CONST = 'const'
    KEBAB = 'kebab'
    LOWER = 'lower'
    PASCAL = 'pascal'
    SNAKE = 'snake'
    TITLE = 'title'
    UPPER = 'upper'


if sys.version_info.major == 2:  # pragma: no cover
    keys = [k for k in Case.__dict__ if not k.startswith('_')]  # pragma: no cover
    CASES = tuple(Case.__dict__[k] for k in keys)  # pragma: no cover
else:
    CASES = tuple(c.value for c in Case.__members__.values())  # type: ignore[attr-defined]


# case patterns

UPPER = r'(?:[A-Z0-9]+)'
LOWER = r'(?:[a-z0-9]+)'
TITLE = rf'(?:[0-9]*[A-Z]{LOWER}?)'

RX_CAMEL = re.compile(f'{LOWER}{TITLE}*')
RX_CONST = re.compile(f'{UPPER}(_{UPPER})*')
RX_KEBAB = re.compile(f'{LOWER}(-{LOWER})*')
RX_LOWER = re.compile(f'{LOWER}( {LOWER})*')
RX_PASCAL = re.compile(f'{TITLE}+')
RX_SNAKE = re.compile(f'{LOWER}(_{LOWER})*')
RX_TITLE = re.compile(f'{TITLE}( {TITLE})*')
RX_UPPER = re.compile(f'{UPPER}( {UPPER})*')


# tokenizer

RX_SIMPLE_SEP = re.compile(r'(_|\W)+')
RX_CASE_SEP1 = re.compile(r'(?P<pre>[a-z][0-9]*)(?P<post>[A-Z])')
RX_CASE_SEP2 = re.compile(r'(?P<pre>[A-Z][0-9]*)(?P<post>[A-Z][0-9]*[a-z])')


def tokenize(text: str) -> str:
    values = RX_SIMPLE_SEP.sub(',', text)
    values = RX_CASE_SEP1.sub(r'\g<pre>,\g<post>', values)
    values = RX_CASE_SEP2.sub(r'\g<pre>,\g<post>', values)
    return values.strip(',')


def words(text: str) -> List[str]:
    return tokenize(text).split(',')


# const case


def is_const(text: str) -> bool:
    return True if RX_CONST.fullmatch(text) else False


def to_const(text: str) -> str:
    return tokenize(text).upper().replace(',', '_')


# camel case


def is_camel(text: str) -> bool:
    return True if RX_CAMEL.fullmatch(text) else False


def to_camel(text: str) -> str:
    wrds = words(text)
    return ''.join([wrds[0].lower(), *(w.title() for w in wrds[1:])])


# kebab case


def is_kebab(text: str) -> bool:
    return True if RX_KEBAB.fullmatch(text) else False


def to_kebab(text: str) -> str:
    return tokenize(text).lower().replace(',', '-')


# lower case


def is_lower(text: str) -> bool:
    return True if RX_LOWER.fullmatch(text) else False


def to_lower(text: str) -> str:
    return tokenize(text).lower().replace(',', ' ')


# pascal case


def is_pascal(text: str) -> bool:
    return True if RX_PASCAL.fullmatch(text) else False


def to_pascal(text: str) -> str:
    return ''.join(w.title() for w in words(text))


# snake case


def is_snake(text: str) -> bool:
    return True if RX_SNAKE.fullmatch(text) else False


def to_snake(text: str) -> str:
    return tokenize(text).lower().replace(',', '_')


# title case


def is_title(text: str) -> bool:
    return True if RX_TITLE.fullmatch(text) else False


def to_title(text: str) -> str:
    return ' '.join(w.title() for w in words(text))


# upper case


def is_upper(text: str) -> bool:
    return True if RX_UPPER.fullmatch(text) else False


def to_upper(text: str) -> str:
    return tokenize(text).upper().replace(',', ' ')


# universal functions


def is_case(case: Union[Case, str], text: str) -> bool:
    case = getattr(case, 'value', case)
    try:
        return {
            'camel': is_camel,
            'const': is_const,
            'kebab': is_kebab,
            'lower': is_lower,
            'pascal': is_pascal,
            'snake': is_snake,
            'title': is_title,
            'upper': is_upper,
        }[str(case)](text)
    except KeyError:
        raise ValueError(f'Unsupported case: {case}')


def to_case(case: Union[Case, str], text: str) -> str:
    case = getattr(case, 'value', case)
    try:
        return {
            'camel': to_camel,
            'const': to_const,
            'kebab': to_kebab,
            'lower': to_lower,
            'pascal': to_pascal,
            'snake': to_snake,
            'title': to_title,
            'upper': to_upper,
        }[str(case)](text)
    except KeyError:
        raise ValueError(f'Unsupported case: {case}')


# cli

parser = ArgumentParser(prog='caseutil', description=__doc__)
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('-c', choices=CASES, required=True)
parser.add_argument('text', default=sys.stdin, nargs='?')


def main() -> None:
    args = parser.parse_args()
    lines = (
        args.text.readlines()
        if isinstance(args.text, TextIOBase)
        else args.text.splitlines()
    )
    values = [to_case(args.c, line) for line in lines]
    print(*values, sep='\n')
