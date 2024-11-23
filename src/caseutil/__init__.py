"""
Case conversion and verification for Python: snake_case, camelCase, kebab-case, etc.
"""

from argparse import ArgumentParser
from io import TextIOBase
import re
import sys
from typing import List, Union

from .__version__ import __version__

__all__ = [
    # verify
    'is_ada',
    'is_camel',
    'is_cobol',
    'is_const',
    'is_kebab',
    'is_lower',
    'is_pascal',
    'is_sentence',
    'is_snake',
    'is_title',
    'is_train',
    'is_upper',
    # convert
    'to_ada',
    'to_camel',
    'to_cobol',
    'to_const',
    'to_kebab',
    'to_lower',
    'to_pascal',
    'to_sentence',
    'to_snake',
    'to_title',
    'to_train',
    'to_upper',
    # universal
    'Case',
    'get_cases',
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


if sys.version_info.major == 2:  # pragma: no cover
    keys = [k for k in Case.__dict__ if not k.startswith('_')]  # pragma: no cover
    CASES = tuple(Case.__dict__[k] for k in keys)  # pragma: no cover
else:
    CASES = tuple(c.value for c in Case.__members__.values())  # type: ignore[attr-defined]


# case patterns

UPPER = r'(?:[A-Z0-9]+)'
LOWER = r'(?:[a-z0-9]+)'
TITLE = rf'(?:[0-9]*[A-Z]{LOWER})'

RX_ADA = re.compile(f'{TITLE}(_{TITLE})*')
RX_CAMEL = re.compile(f'{LOWER}{TITLE}*')
RX_COBOL = re.compile(f'{UPPER}(-{UPPER})*')
RX_CONST = re.compile(f'{UPPER}(_{UPPER})*')
RX_KEBAB = re.compile(f'{LOWER}(-{LOWER})*')
RX_LOWER = re.compile(f'{LOWER}( {LOWER})*')
RX_PASCAL = re.compile(f'{TITLE}+')
RX_SENTENCE = re.compile(f'{TITLE}( {LOWER})*')
RX_SNAKE = re.compile(f'{LOWER}(_{LOWER})*')
RX_TITLE = re.compile(f'{TITLE}( {TITLE})*')
RX_TRAIN = re.compile(f'{TITLE}(-{TITLE})*')
RX_UPPER = re.compile(f'{UPPER}( {UPPER})*')


# tokenizer

RX_SIMPLE_SEP = re.compile(r'(_|\W)+')
RX_CASE_SEP1 = re.compile(r'(?P<pre>[a-z][0-9]*)(?P<post>[A-Z])')
RX_CASE_SEP2 = re.compile(r'(?P<pre>[A-Z][0-9]*)(?P<post>[A-Z][0-9]*[a-z])')


def tokenize(text: str) -> str:
    values = RX_SIMPLE_SEP.sub(' ', text)
    values = RX_CASE_SEP1.sub(r'\g<pre> \g<post>', values)
    values = RX_CASE_SEP2.sub(r'\g<pre> \g<post>', values)
    return values.strip()


def words(text: str) -> List[str]:
    return tokenize(text).split()


# ada case


def is_ada(text: str) -> bool:
    return True if RX_ADA.fullmatch(text) else False


def to_ada(text: str) -> str:
    wrds = words(text)
    return '_'.join(w.title() for w in wrds)


# camel case


def is_camel(text: str) -> bool:
    return True if RX_CAMEL.fullmatch(text) else False


def to_camel(text: str) -> str:
    wrds = words(text)
    if not wrds:
        return ''
    return ''.join([wrds[0].lower(), *(w.title() for w in wrds[1:])])


# cobol case


def is_cobol(text: str) -> bool:
    return True if RX_COBOL.fullmatch(text) else False


def to_cobol(text: str) -> str:
    return tokenize(text).upper().replace(' ', '-')


# const case


def is_const(text: str) -> bool:
    return True if RX_CONST.fullmatch(text) else False


def to_const(text: str) -> str:
    return tokenize(text).upper().replace(' ', '_')


# kebab case


def is_kebab(text: str) -> bool:
    return True if RX_KEBAB.fullmatch(text) else False


def to_kebab(text: str) -> str:
    return tokenize(text).lower().replace(' ', '-')


# lower case


def is_lower(text: str) -> bool:
    return True if RX_LOWER.fullmatch(text) else False


def to_lower(text: str) -> str:
    return tokenize(text).lower().replace(' ', ' ')


# pascal case


def is_pascal(text: str) -> bool:
    return True if RX_PASCAL.fullmatch(text) else False


def to_pascal(text: str) -> str:
    return ''.join(w.title() for w in words(text))


# sentence case


def is_sentence(text: str) -> bool:
    return True if RX_SENTENCE.fullmatch(text) else False


def to_sentence(text: str) -> str:
    wrds = words(text)
    if not wrds:
        return ''
    return ' '.join([wrds[0].title(), *(w.lower() for w in wrds[1:])])


# snake case


def is_snake(text: str) -> bool:
    return True if RX_SNAKE.fullmatch(text) else False


def to_snake(text: str) -> str:
    return tokenize(text).lower().replace(' ', '_')


# title case


def is_title(text: str) -> bool:
    return True if RX_TITLE.fullmatch(text) else False


def to_title(text: str) -> str:
    return ' '.join(w.title() for w in words(text))


# train case


def is_train(text: str) -> bool:
    return True if RX_TRAIN.fullmatch(text) else False


def to_train(text: str) -> str:
    wrds = words(text)
    return '-'.join(w.title() for w in wrds)


# upper case


def is_upper(text: str) -> bool:
    return True if RX_UPPER.fullmatch(text) else False


def to_upper(text: str) -> str:
    return tokenize(text).upper().replace(' ', ' ')


# universal functions


def is_case(case: Union[Case, str], text: str) -> bool:
    case = getattr(case, 'value', case)
    try:
        return {
            'ada': is_ada,
            'camel': is_camel,
            'cobol': is_cobol,
            'const': is_const,
            'kebab': is_kebab,
            'lower': is_lower,
            'pascal': is_pascal,
            'sentence': is_sentence,
            'snake': is_snake,
            'title': is_title,
            'train': is_train,
            'upper': is_upper,
        }[str(case)](text)
    except KeyError:
        raise ValueError(f'Unsupported case: {case}')


def to_case(case: Union[Case, str], text: str) -> str:
    case = getattr(case, 'value', case)
    try:
        return {
            'ada': to_ada,
            'camel': to_camel,
            'cobol': to_cobol,
            'const': to_const,
            'kebab': to_kebab,
            'lower': to_lower,
            'pascal': to_pascal,
            'sentence': to_sentence,
            'snake': to_snake,
            'title': to_title,
            'train': to_train,
            'upper': to_upper,
        }[str(case)](text)
    except KeyError:
        raise ValueError(f'Unsupported case: {case}')


def get_cases(text: str) -> tuple[str, ...]:
    return tuple(c for c in CASES if is_case(c, text))


# cli

parser = ArgumentParser(prog='caseutil', description=__doc__)
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('text', default=sys.stdin, nargs='?')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-c', '--convert', choices=CASES)
group.add_argument('-d', '--detect', action='store_true')


def main() -> None:
    args = parser.parse_args()

    def lines(source) -> str:
        if isinstance(source, TextIOBase):
            yield from source
        elif isinstance(source, str):
            yield from source.splitlines()
        else:
            raise TypeError('Unsupported source type')  # pragma: no cover

    if args.convert:
        for line in lines(args.text):
            print(to_case(args.convert, line))
    if args.detect:
        for line in lines(args.text):
            print(' '.join(get_cases(line)))
    sys.exit(0)
