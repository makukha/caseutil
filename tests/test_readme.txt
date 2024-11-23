>>> from caseutil import *

>>> is_snake('Foo bar-baz')
False

>>> to_snake('Foo bar-baz')
'foo_bar_baz'

>>> is_case(Case.CAMEL, 'myVarName')
True
>>> to_case(Case.CONST, 'myVarName')
'MY_VAR_NAME'

>>> get_cases('fooBar')
('camel',)
>>> get_cases('My var-name')  # mixed case
()
>>> get_cases('Title')
('ada', 'pascal', 'sentence', 'title', 'train')

>>> '/'.join(words(to_lower('myVarName')))
'my/var/name'
>>> '.'.join(words('myVarName'))
'my.Var.Name'

>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']

