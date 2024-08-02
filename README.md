# caseutil ⇄ 🐍🐫🍢
[![license](https://img.shields.io/github/license/makukha/caseutil.svg)](https://github.com/makukha/caseutil/blob/main/LICENSE)
[![Tests](https://raw.githubusercontent.com/makukha/caseutil/0.6.1/docs/badge/tests.svg)](https://github.com/makukha/caseutil)
[![Coverage](https://raw.githubusercontent.com/makukha/caseutil/0.6.1/docs/badge/coverage.svg)](https://github.com/makukha/caseutil)
[![pypi](https://img.shields.io/pypi/v/caseutil.svg)](https://pypi.python.org/pypi/caseutil)
[![versions](https://img.shields.io/pypi/pyversions/caseutil.svg)](https://pypi.org/project/caseutil)

Case convert and verify for Python: snake_case, camelCase, kebab-case, and more.


## Features

* Verify and convert between most popular cases
* Custom separators: `'my.variable.name'`, `'my/variable/name'`
* Command line mode: `caseutil`
* Pure Python 2.7 to 3.13+
* No dependencies
* 100% test coverage


## Supported Cases

| Case        | Example          | Functions                |
|-------------|------------------|--------------------------|
| snake_case  | my_variable_name | `is_snake`, `to_snake`   |
| CONST_CASE  | MY_VARIABLE_NAME | `is_const`, `to_const`   |
| camelCase   | myVariableName   | `is_camel`, `to_camel`   |
| PascalCase  | MyVariableName   | `is_pascal`, `to_pascal` |
| kebab-case  | my-variable-name | `is_kebab`, `to_kebab`   |
| lower space | my variable name | `is_lower`, `to_lower`   |
| UPPER SPACE | MY VARIABLE NAME | `is_upper`, `to_upper`   |
| Title Space | My Variable Name | `is_title`, `to_title`   |


## Installation

```bash
$ pip install caseutil
```

## Quick Start

```doctest
>>> from caseutil import *
```

Verify case format:
```doctest
>>> is_snake('My variable-name')
False
```

Convert to case:
```doctest
>>> to_snake('My variable-name')
'my_variable_name'
```

Use as command line tool, supports multiple values in argument or stdin:
```bash
$ caseutil -c const "hi there"
HI_THERE
$ echo "hi_there\nsee you" | python -m caseutil -c camel
hiThere
seeYou
```


## Universal Functions

Use functions `is_case()` and `to_case()` to deal with arbitrary case:
```doctest
>>> is_case('camel', 'myVariableName')
True
>>> to_case(Case.CONST, 'myVariableName')
'MY_VARIABLE_NAME'
```

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


## Tokenization

Word separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators. For more details, see this example and unit tests.

```doctest
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
```

## Custom Separators

For custom separators, use `words()` function:
```doctest
>>> '/'.join(words(to_lower('myVariableName')))
'my/variable/name'
>>> '.'.join(words('myVariableName'))
'my.Variable.Name'
```


## Unicode

Only ASCII names are supported. Unicode support is planned.


## Developer Notes

### Mac OS X

This project requires [Homebrew](https://brew.sh). Other tools like [PDM](https://pdm-project.org), [Tox](https://tox.wiki), and even [Alacritty](https://alacritty.org), will be installed automatically.

```bash
git clone https://github.com/makukha/caseutil.git
cd caseutil
brew bundle
task init install
```

### Operations

| Command        | Description                   |
|----------------|-------------------------------|
| `task init`    | Initialize system environment |
| `task install` | Install Python environment    |
| `task test`    | Run tests                     |


### Plans

* Add more test, explore edge cases
* Add Unicode support (write tests)
* Add more cases
