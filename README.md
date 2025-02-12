<!-- docsub: begin -->
<!-- docsub: include docs/part/title.md -->
# caseutil ⇄ 🐍🐫🍢
> Case conversion and verification for Python: snake_case, camelCase, kebab-case, etc.
<!-- docsub: end -->

<!-- docsub: begin -->
<!-- docsub: include docs/part/badges.md -->
[![license](https://img.shields.io/github/license/makukha/caseutil.svg)](https://github.com/makukha/caseutil/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/caseutil.svg#v0.7.1)](https://pypi.python.org/pypi/caseutil)
[![python versions](https://img.shields.io/pypi/pyversions/caseutil.svg)](https://pypi.org/project/caseutil)
[![tests](https://raw.githubusercontent.com/makukha/caseutil/v0.7.1/docs/badge/tests.svg)](https://github.com/makukha/caseutil)
[![coverage](https://raw.githubusercontent.com/makukha/caseutil/v0.7.1/docs/badge/coverage.svg)](https://github.com/makukha/caseutil)
[![tested with multipython](https://img.shields.io/badge/tested_with-multipython-x)](https://github.com/makukha/multipython)
[![docs status](https://readthedocs.org/projects/caseutil/badge/?version=latest)](https://caseutil.readthedocs.io/en/latest/?badge=latest)
[![uses docsub](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/makukha/docsub/refs/heads/main/docs/badge/v1.json)](https://github.com/makukha/docsub)
[![mypy](https://img.shields.io/badge/type_checked-mypy-%231674b1)](http://mypy.readthedocs.io)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![openssf best practices](https://www.bestpractices.dev/projects/9342/badge)](https://www.bestpractices.dev/projects/9342)
<!-- docsub: end -->

# Features

<!-- docsub: begin -->
<!-- docsub: include docs/part/features.md -->
* Verify and convert between most popular cases
* Custom separators: `'foo.bar.baz'`, `'foo/bar/baz'`
* Case detection
* Command line utility `caseutil`
* Pure Python 2.7 to 3.14+
* No dependencies
* 100% test coverage
<!-- docsub: end -->

## Supported cases

### [Classification](https://caseutil.readthedocs.io/en/latest/classification/)

![Cases classification](docs/img/classification-dark.svg#gh-dark-mode-only)
![Cases classification](docs/img/classification-default.svg#gh-light-mode-only)

<!-- docsub: begin -->
<!-- docsub: include docs/part/cases-table.md -->
| Case          | Verify        | Convert       |
|---------------|---------------|---------------|
| snake_case    | `is_snake`    | `to_snake`    |
| Ada_Case      | `is_ada`      | `to_ada`      |
| CONST_CASE    | `is_const`    | `to_const`    |
| camelCase     | `is_camel`    | `to_camel`    |
| PascalCase    | `is_pascal`   | `to_pascal`   |
| kebab-case    | `is_kebab`    | `to_kebab`    |
| Train-Case    | `is_train`    | `to_train`    |
| COBOL-CASE    | `is_cobol`    | `to_cobol`    |
| lower case    | `is_lower`    | `to_lower`    |
| UPPER CASE    | `is_upper`    | `to_upper`    |
| Title Case    | `is_title`    | `to_title`    |
| Sentence case | `is_sentence` | `to_sentence` |
<!-- docsub: end -->

# Installation

```shell
$ pip install caseutil
```

<!-- docsub: begin #usage.md -->
<!-- docsub: include docs/part/usage.md -->
## Use cases

<!-- docsub: begin -->
<!-- docsub: x caselist tests/test_usage.py -->
* [Basic usage](#basic-usage)
* [Cases enum](#cases-enum)
* [Arbitrary cases](#arbitrary-cases)
* [Detect cases](#detect-cases)
* [Custom separators](#custom-separators)
* [Tokenization](#tokenization)
* [Unicode support *(not implemented)*](#unicode-support-not-implemented)
<!-- docsub: end -->

<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:BasicUsage -->
### Basic usage

```pycon
>>> from caseutil import is_snake, to_snake

>>> is_snake('Foo bar-baz')
False

>>> to_snake('Foo bar-baz')
'foo_bar_baz'
```
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:CasesEnum -->
### Cases enum

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
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:ArbitraryCases -->
### Arbitrary cases

Use functions `is_case()` and `to_case()` to deal with arbitrary supported case:

```pycon
>>> from caseutil import Case, is_case, to_case

>>> is_case(Case.CAMEL, 'myVarName')
True

>>> to_case(Case.CONST, 'myVarName')
'MY_VAR_NAME'
```
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:DetectCases -->
### Detect cases

Use function `get_cases()` to determine case (or cases, if
[ambiguous](https://caseutil.readthedocs.io/en/latest/classification/#ambiguity)):

```pycon
>>> from caseutil import get_cases

>>> get_cases('fooBar')
('camel',)

>>> get_cases('My var-name')  # mixed case
()

>>> get_cases('Title')  # matches multiple cases
('ada', 'pascal', 'sentence', 'title', 'train')
```
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:CustomSeparators -->
### Custom separators

Use fiunction`words()`:

```pycon
>>> from caseutil import words, to_lower

>>> '/'.join(words(to_lower('myVarName')))
'my/var/name'

>>> '.'.join(words('myVarName'))
'my.Var.Name'
```
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:Tokenization -->
### Tokenization

Word separators are non-word characters including underscore, and places where
text case is changed from lower to upper. Digits are not treated as separators.
For more details, see
[Tokenization rules](https://caseutil.readthedocs.io/en/latest/tokenize).

```pycon
>>> from caseutil import words

>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
```
<!-- docsub: end -->


<!-- docsub: begin -->
<!-- docsub: x case tests/test_usage.py:UnicodeSupport -->
### Unicode support *(not implemented)*

Only ASCII names are supported. Unicode support is planned.
<!-- docsub: end -->
<!-- docsub: end #usage.md -->


<!-- docsub: begin #cli.md -->
<!-- docsub: include docs/part/cli.md -->
## Command line

```shell
$ caseutil -c const "hi there"
HI_THERE
```

Invoke as Python module:
```shell
$ python -m caseutil -c const "hi there"
HI_THERE
```

When reading from stdin, each line is processed separately:
```shell
$ echo "hi_there\nsee you" | python -m caseutil -c camel
hiThere
seeYou
```

### CLI Reference

<!-- docsub: begin #caseutil-help -->
<!-- docsub: help caseutil -->
<!-- docsub: lines after 2 upto -1 -->
```text
$ caseutil --help
usage: caseutil [-h] (--version | -c <case> | -d) [text]

  Convert, detect, or match text case.

  When stdin is used as input, each line is tokenized and processed separately.

cases:
  ada,camel,cobol,const,kebab,lower,pascal,sentence,snake,title,train,upper

positional arguments:
  text                  text to be converted; if missing, stdin is used

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c, --convert <case>  convert [text] or stdin to <case>
  -d, --detect          detect cases in [text] or stdin
```
<!-- docsub: end #caseutil-help -->
<!-- docsub: end #cli.md -->


# Alternatives

[70+ packages](https://caseutil.readthedocs.io/en/latest/alternatives/)

# Contributing

See [Contributing](.github/CONTRIBUTING.md) guidelines.

# Authors

* [Michael Makukha](https://github.com/makukha)


## See also

* [Project changelog](https://github.com/makukha/caseutil/tree/main/CHANGELOG.md)
