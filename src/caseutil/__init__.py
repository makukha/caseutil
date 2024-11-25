"""
Case conversion and verification for Python: snake_case, camelCase, kebab-case, etc.
"""

from argparse import ArgumentParser
import re
import sys

try:
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:  # pragma: no cover
        from typing import List, Tuple, Union  # noqa: F401
except ImportError:  # pragma: no cover
    pass

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

    class _Case:
        pass
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
TITLE = r'(?:[0-9]*[A-Z]' + LOWER + ')'

LUT = {'LOWER': LOWER, 'UPPER': UPPER, 'TITLE': TITLE}

RX_ADA = re.compile('^{TITLE}(_{TITLE})*$'.format(**LUT))
RX_CAMEL = re.compile('^{LOWER}{TITLE}*$'.format(**LUT))
RX_COBOL = re.compile('^{UPPER}(-{UPPER})*$'.format(**LUT))
RX_CONST = re.compile('^{UPPER}(_{UPPER})*$'.format(**LUT))
RX_KEBAB = re.compile('^{LOWER}(-{LOWER})*$'.format(**LUT))
RX_LOWER = re.compile('^{LOWER}( {LOWER})*$'.format(**LUT))
RX_PASCAL = re.compile('^{TITLE}+$'.format(**LUT))
RX_SENTENCE = re.compile('^{TITLE}( {LOWER})*$'.format(**LUT))
RX_SNAKE = re.compile('^{LOWER}(_{LOWER})*$'.format(**LUT))
RX_TITLE = re.compile('^{TITLE}( {TITLE})*$'.format(**LUT))
RX_TRAIN = re.compile('^{TITLE}(-{TITLE})*$'.format(**LUT))
RX_UPPER = re.compile('^{UPPER}( {UPPER})*$'.format(**LUT))


# tokenizer

RX_SIMPLE_SEP = re.compile(r'(_|\W)+')
RX_CASE_SEP1 = re.compile(r'(?P<pre>[a-z][0-9]*)(?P<post>[A-Z])')
RX_CASE_SEP2 = re.compile(r'(?P<pre>[A-Z][0-9]*)(?P<post>[A-Z][0-9]*[a-z])')


def tokenize(text):
    # type: (str) -> str
    values = RX_SIMPLE_SEP.sub(' ', text)
    values = RX_CASE_SEP1.sub(r'\g<pre> \g<post>', values)
    values = RX_CASE_SEP2.sub(r'\g<pre> \g<post>', values)
    return values.strip()


def words(text):
    # type: (str) -> List[str]
    return tokenize(text).split()


# ada case


def is_ada(text):
    # type: (str) -> bool
    return True if RX_ADA.match(text) else False


def to_ada(text):
    # type: (str) -> str
    wrds = words(text)
    return '_'.join(w.title() for w in wrds)


# camel case


def is_camel(text):
    # type: (str) -> bool
    return True if RX_CAMEL.match(text) else False


def to_camel(text):
    # type: (str) -> str
    wrds = words(text)
    if not wrds:
        return ''
    return ''.join([w.lower() if i == 0 else w.title() for i, w in enumerate(wrds)])


# cobol case


def is_cobol(text):
    # type: (str) -> bool
    return True if RX_COBOL.match(text) else False


def to_cobol(text):
    # type: (str) -> str
    return tokenize(text).upper().replace(' ', '-')


# const case


def is_const(text):
    # type: (str) -> bool
    return True if RX_CONST.match(text) else False


def to_const(text):
    # type: (str) -> str
    return tokenize(text).upper().replace(' ', '_')


# kebab case


def is_kebab(text):
    # type: (str) -> bool
    return True if RX_KEBAB.match(text) else False


def to_kebab(text):
    # type: (str) -> str
    return tokenize(text).lower().replace(' ', '-')


# lower case


def is_lower(text):
    # type: (str) -> bool
    return True if RX_LOWER.match(text) else False


def to_lower(text):
    # type: (str) -> str
    return tokenize(text).lower().replace(' ', ' ')


# pascal case


def is_pascal(text):
    # type: (str) -> bool
    return True if RX_PASCAL.match(text) else False


def to_pascal(text):
    # type: (str) -> str
    return ''.join(w.title() for w in words(text))


# sentence case


def is_sentence(text):
    # type: (str) -> bool
    return True if RX_SENTENCE.match(text) else False


def to_sentence(text):
    # type: (str) -> str
    wrds = words(text)
    if not wrds:
        return ''
    return ' '.join([w.title() if i == 0 else w.lower() for i, w in enumerate(wrds)])


# snake case


def is_snake(text):
    # type: (str) -> bool
    return True if RX_SNAKE.match(text) else False


def to_snake(text):
    # type: (str) -> str
    return tokenize(text).lower().replace(' ', '_')


# title case


def is_title(text):
    # type: (str) -> bool
    return True if RX_TITLE.match(text) else False


def to_title(text):
    # type: (str) -> str
    return ' '.join(w.title() for w in words(text))


# train case


def is_train(text):
    # type: (str) -> bool
    return True if RX_TRAIN.match(text) else False


def to_train(text):
    # type: (str) -> str
    wrds = words(text)
    return '-'.join(w.title() for w in wrds)


# upper case


def is_upper(text):
    # type: (str) -> bool
    return True if RX_UPPER.match(text) else False


def to_upper(text):
    # type: (str) -> str
    return tokenize(text).upper().replace(' ', ' ')


# universal functions


def is_case(case, text):
    # type: (Union[Case, str], str) -> bool
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
        raise ValueError('Unsupported case: {}'.format(case))


def to_case(case, text):
    # type: (Union[Case, str], str) -> str
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
        raise ValueError('Unsupported case: {}'.format(case))


def get_cases(text):
    # type: (str) -> Tuple[str, ...]
    return tuple(sorted(c for c in CASES if is_case(c, text)))


# cli

parser = ArgumentParser(prog='caseutil', description=__doc__)
parser.add_argument('text', default=sys.stdin, nargs='?')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--version', action='store_true')
group.add_argument('-c', '--convert', choices=CASES)
group.add_argument('-d', '--detect', action='store_true')


def main():
    # type: () -> None
    args = parser.parse_args()

    if args.version:
        print('caseutil ' + __version__)
        sys.exit(0)

    def lines(source):  # type: ignore[misc]
        if hasattr(source, 'readline'):
            for line in source:
                yield line
        elif isinstance(source, str):
            for line in source.splitlines():
                yield line
        else:
            raise TypeError('Unsupported source type')  # pragma: no cover

    if args.convert:
        for line in lines(args.text):
            print(to_case(args.convert, line))
    if args.detect:
        for line in lines(args.text):
            print(' '.join(get_cases(line)))
    sys.exit(0)
