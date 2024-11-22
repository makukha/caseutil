# caseutil ⇄ 🐍🐫🍢
> Case conversion and verification for Python: snake_case, camelCase, kebab-case, etc.

[![versions](https://img.shields.io/pypi/pyversions/caseutil.svg)](https://pypi.org/project/caseutil)  
[![pypi](https://img.shields.io/pypi/v/caseutil.svg#v0.6.5)](https://pypi.python.org/pypi/caseutil)
[![Tests](https://raw.githubusercontent.com/makukha/caseutil/v0.6.5/docs/badge/tests.svg)](https://github.com/makukha/caseutil)
[![Coverage](https://raw.githubusercontent.com/makukha/caseutil/v0.6.5/docs/badge/coverage.svg)](https://github.com/makukha/caseutil)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/caseutil)](https://pypistats.org/packages/caseutil)  
[![license](https://img.shields.io/github/license/makukha/caseutil.svg)](https://github.com/makukha/caseutil/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/caseutil/badge/?version=latest)](https://caseutil.readthedocs.io/en/latest/?badge=latest)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9342/badge)](https://www.bestpractices.dev/projects/9342)

## Features

* Verify and convert between most popular cases
* Custom separators: `'foo.bar.baz'`, `'foo/bar/baz'`
* Command line utility `caseutil`
* Pure Python 2.7 to 3.14+
* No dependencies
* 100% test coverage

### Supported cases

| Case       | Verify      | Convert     |
|------------|-------------|-------------|
| snake_case | `is_snake`  | `to_snake`  |
| CONST_CASE | `is_const`  | `to_const`  |
| camelCase  | `is_camel`  | `to_camel`  |
| PascalCase | `is_pascal` | `to_pascal` |
| kebab-case | `is_kebab`  | `to_kebab`  |
| lower case | `is_lower`  | `to_lower`  |
| UPPER CASE | `is_upper`  | `to_upper`  |
| Title Case | `is_title`  | `to_title`  |

## Installation

```shell
$ pip install caseutil
```

## Simple usage

```doctest
>>> from caseutil import *

>>> is_snake('Foo bar-baz')
False

>>> to_snake('Foo bar-baz')
'foo_bar_baz'
```

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

## Advanced usage

### Cases enum

All supported cases are gathered in `Case` enum:
```python
class Case(StrEnum):
    CAMEL = 'camel'
    CONST = 'const'
    KEBAB = 'kebab'
    LOWER = 'lower'
    PASCAL = 'pascal'
    SNAKE = 'snake'
    TITLE = 'title'
    UPPER = 'upper'
```

### Universal operations

Use functions `is_case()` and `to_case()` to deal with any supported case:

```doctest
>>> is_case(Case.CAMEL, 'myVariableName')
True
>>> to_case(Case.CONST, 'myVariableName')
'MY_VARIABLE_NAME'
```

### Custom separators

Use `words()` function:

```doctest
>>> '/'.join(words(to_lower('myVariableName')))
'my/variable/name'
>>> '.'.join(words('myVariableName'))
'my.Variable.Name'
```

### Tokenization

Word separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators. For more details, see [Tokenization rules](./tokenize/).

```doctest
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
```

### Unicode support

Only ASCII names are supported. Unicode support is planned.

## Development

This project requires [Docker](https://www.docker.com).

```shell
git clone https://github.com/makukha/caseutil.git
cd caseutil
task dev
```

```shell
root@caseutil:/project# task lint
root@caseutil:/project# task format
root@caseutil:/project# task test
```

## Contributing

See [Contributing](https://github.com/makukha/caseutil/blob/main/.github/CONTRIBUTING.md) guidelines.

## Authors

* [Michael Makukha](https://github.com/makukha)

## License

[MIT License](https://github.com/makukha/caseutil/blob/main/LICENSE)
