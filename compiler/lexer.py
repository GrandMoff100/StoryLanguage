from ply import lex
from .errors import SyntaxAnomaly
from .tokens import tokens


# Tokens
t_NAMESPACE = '[A-Z][a-z]+'
t_VARIABLEASSIGNMENT = 'is'
t_UNKNOWNLOCATION = '(over\s(there|here))|(there|here)'
t_EXPLICITLOCATION = 'at'
t_LOCATIONTRANSITION = 'went\sto|moved\sto|is\sgoing\sto'
t_EXISTINGREFERENCE = 'the'
t_NEWREFERENCE = 'a'
t_LOCATIONQUERY = 'Where\sis'
T_GETMOSTRECENTVARIABLE = 'him|her|them|it'
t_SETMOSTRECENTVARIABLE = 'He|She|They|It'

# Comment tokens
def t_INLINECOMMENT(t):
    r'\#.*\n'
    pass

def t_MULTILINECOMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

# Utility Expressions
t_ignore  = ' \t,?!'

# General Handlers
def t_newline(t):
    r'\n+|(\.\s)+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    err = SyntaxAnomaly('Illegal Character', t.value[0])
    err.run()


lexer = lex.lex()

