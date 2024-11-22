>>> from caseutil import *

>>> is_snake('Foo bar-baz')
False

>>> to_snake('Foo bar-baz')
'foo_bar_baz'

>>> is_case(Case.CAMEL, 'myVariableName')
True
>>> to_case(Case.CONST, 'myVariableName')
'MY_VARIABLE_NAME'

>>> '/'.join(words(to_lower('myVariableName')))
'my/variable/name'
>>> '.'.join(words('myVariableName'))
'my.Variable.Name'

>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']

