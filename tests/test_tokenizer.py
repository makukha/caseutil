from unittest import TestCase

from doctestcase import doctestcase


@doctestcase()
class TokenizationRules(TestCase):
    r"""
    Tokenization rules

    >>> from caseutil import tokenize

    Text is tokenized as space separated words list, preserving case.

    >>> tokenize('Space-separated,phrase')
    'Space separated phrase'

    Digit is a part of the word:

    >>> tokenize('some_0_Digits111')
    'some 0 Digits111'

    All non-word characters including underscore are word separators:

    >>> ascii = ''.join(str(chr(c)) for c in range(256))
    >>> import re
    >>> sep = '_' + re.sub(r'\w', '', ascii)
    >>> set(tokenize('Word1' + s + 'Word2') for s in sep) == {'Word1 Word2'}
    True

    When text case is changed from lower to upper, this is also a word separator, but
    case change from upper to lower is not:

    >>> tokenize('ErrorType')
    'Error Type'

    When case is changed from lower to upper and there are digits in between,
    separator is added after the digits:

    >>> tokenize('Http404Error')
    'Http404 Error'
    >>> tokenize('Http404error')
    'Http404error'

    If there are multiple upper case letters followed by a lower case, the separator is
    inserted before the last upper letter:

    >>> tokenize('HTTPError')
    'HTTP Error'
    >>> tokenize('HTTP2Error')
    'HTTP2 Error'

    Initial and trailing separators are stripped:

    >>> tokenize('_some_name_')
    'some name'

    Multiple separators are treated as one:

    >>> tokenize('some-._name')
    'some name'

    Empty string remains itself:

    >>> tokenize('')
    ''
    """
