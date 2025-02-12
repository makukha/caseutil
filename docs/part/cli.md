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
