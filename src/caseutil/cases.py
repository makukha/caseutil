import re
import sys


if sys.version_info.major == 2:  # pragma: no cover

    class CaseEnumBase:
        pass

else:
    from enum import Enum

    class CaseEnumBase(str, Enum):
        pass


class Case(CaseEnumBase):
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

    @classmethod
    def as_tuple(cls):
        return tuple(
            getattr(v, 'value', v)
            for k, v in vars(cls).items()
            if not k.startswith('_') and not isinstance(v, classmethod)
        )


# case patterns

UPPER = r'(?:[A-Z0-9]+)'
LOWER = r'(?:[a-z0-9]+)'
TITLE = r'(?:[0-9]*[A-Z](?:' + LOWER + '|$))'

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
    values = RX_SIMPLE_SEP.sub(' ', text)
    values = RX_CASE_SEP1.sub(r'\g<pre> \g<post>', values)
    values = RX_CASE_SEP2.sub(r'\g<pre> \g<post>', values)
    return values.strip()


def words(text):
    return tokenize(text).split()


# ada case


def is_ada(text):
    return True if RX_ADA.match(text) else False


def to_ada(text):
    wrds = words(text)
    return '_'.join(w.title() for w in wrds)


# camel case


def is_camel(text):
    return True if RX_CAMEL.match(text) else False


def to_camel(text):
    wrds = words(text)
    if not wrds:
        return ''
    return ''.join([w.lower() if i == 0 else w.title() for i, w in enumerate(wrds)])


# cobol case


def is_cobol(text):
    return True if RX_COBOL.match(text) else False


def to_cobol(text):
    return tokenize(text).upper().replace(' ', '-')


# const case


def is_const(text):
    return True if RX_CONST.match(text) else False


def to_const(text):
    return tokenize(text).upper().replace(' ', '_')


# kebab case


def is_kebab(text):
    return True if RX_KEBAB.match(text) else False


def to_kebab(text):
    return tokenize(text).lower().replace(' ', '-')


# lower case


def is_lower(text):
    return True if RX_LOWER.match(text) else False


def to_lower(text):
    # type: (str) -> str
    return tokenize(text).lower().replace(' ', ' ')


# pascal case


def is_pascal(text):
    return True if RX_PASCAL.match(text) else False


def to_pascal(text):
    return ''.join(w.title() for w in words(text))


# sentence case


def is_sentence(text):
    return True if RX_SENTENCE.match(text) else False


def to_sentence(text):
    wrds = words(text)
    if not wrds:
        return ''
    return ' '.join([w.title() if i == 0 else w.lower() for i, w in enumerate(wrds)])


# snake case


def is_snake(text):
    return True if RX_SNAKE.match(text) else False


def to_snake(text):
    return tokenize(text).lower().replace(' ', '_')


# title case


def is_title(text):
    return True if RX_TITLE.match(text) else False


def to_title(text):
    return ' '.join(w.title() for w in words(text))


# train case


def is_train(text):
    return True if RX_TRAIN.match(text) else False


def to_train(text):
    wrds = words(text)
    return '-'.join(w.title() for w in wrds)


# upper case


def is_upper(text):
    return True if RX_UPPER.match(text) else False


def to_upper(text):
    return tokenize(text).upper().replace(' ', ' ')


# universal functions


def is_case(case, text):
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
        raise ValueError('Unsupported case: {}'.format(case))  # noqa: B904


def to_case(case, text):
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
        raise ValueError('Unsupported case: {}'.format(case))  # noqa: B904


def get_cases(text):
    return tuple(sorted(c for c in Case.as_tuple() if is_case(c, text)))
