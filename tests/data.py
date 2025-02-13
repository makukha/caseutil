from caseutil import Case


def tostr(item):  # type: (object) -> object
    return getattr(item, 'value', item)


# my-var-name example

X_MVN_IN = 'My var-name'
X_MVN_OUT = (
    (tostr(Case.ADA), 'My_Var_Name'),
    (tostr(Case.CAMEL), 'myVarName'),
    (tostr(Case.COBOL), 'MY-VAR-NAME'),
    (tostr(Case.CONST), 'MY_VAR_NAME'),
    (tostr(Case.KEBAB), 'my-var-name'),
    (tostr(Case.LOWER), 'my var name'),
    (tostr(Case.PASCAL), 'MyVarName'),
    (tostr(Case.SENTENCE), 'My var name'),
    (tostr(Case.SNAKE), 'my_var_name'),
    (tostr(Case.TITLE), 'My Var Name'),
    (tostr(Case.TRAIN), 'My-Var-Name'),
    (tostr(Case.UPPER), 'MY VAR NAME'),
)

assert len(X_MVN_OUT) == len(Case.as_tuple())


# mixed case

X_MIXED = 'My var-name'


# ambiguous cases

X_AMBIGUOUS = (
    # single word
    ('lower', 'camel kebab lower snake'),
    ('Title', 'ada pascal sentence title train'),
    ('UPPER', 'cobol const upper'),
    # single character
    ('l', 'camel kebab lower snake'),
    ('U', 'ada cobol const pascal sentence title train upper'),
)
