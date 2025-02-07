## Basic usage

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

### CLI Reference

<!-- docsub: begin #cli -->
<!-- docsub: help caseutil -->
<!-- docsub: lines after 2 upto -1 -->
```shell
$ caseutil --help
usage: caseutil [-h] (--version | -c <case> | -d) [text]

Convert, detect, or match text case.

When stdin is used as input, each line is tokenized and processed separately.

<case> choices:
  ada,camel,cobol,const,kebab,lower,pascal,sentence,snake,title,train,upper

positional arguments:
  text                  text to be converted; if missing, stdin is used

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c, --convert <case>  convert [text] or stdin to <case>
  -d, --detect          detect cases in [text] or stdin
```
<!-- docsub: end #cli -->


## Advanced usage

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

### Universal operations

Use functions `is_case()` and `to_case()` to deal with any supported case:

```doctest
>>> is_case(Case.CAMEL, 'myVarName')
True
>>> to_case(Case.CONST, 'myVarName')
'MY_VAR_NAME'
```

### Cases detection

Use `get_cases()` function to determine case (or cases, if [ambiguous](classification.md#ambiguity)):

```doctest
>>> get_cases('fooBar')
('camel',)
>>> get_cases('My var-name')  # mixed case
()
>>> get_cases('Title')
('ada', 'pascal', 'sentence', 'title', 'train')
```

### Custom separators

Use `words()` function:

```doctest
>>> '/'.join(words(to_lower('myVarName')))
'my/var/name'
>>> '.'.join(words('myVarName'))
'my.Var.Name'
```

### Tokenization

Word separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators. For more details, see [Tokenization rules](tokenize.md).

```doctest
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
```

### Unicode support

Only ASCII names are supported. Unicode support is planned.
