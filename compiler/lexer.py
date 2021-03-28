from ply import lex
from .errors import SyntaxAnomaly
from .tokens import tokens


# Tokens
t_NAMESPACE = '[A-Z][a-z]+'
t_VARIABLEASSIGNMENT = 'is'
t_UNKNOWNPOSITION = 'over\sthere|here'
t_EXPLICITPOSITION = 'at'
t_POSITIONCHANGE = 'went\sto|moved\sto|is\sgoing\sto'
t_EXISTINGREFERENCE = 'the'
t_NEWREFERENCE = 'a'
t_LOCATIONQUERY = 'where\sis'


# Comment tokens
def t_INLINECOMMENT(self, t):
    r'\#.*\n'
    pass

def t_MULTILINECOMMENT(self, t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

# Utility Expressions
t_ignore  = ' \t.,?!'

# General Handlers
def t_newline(self, t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(self, t):
    err = SyntaxAnomaly('Illegal Character', t.value[0])
    err.run()


lexer = lex.lex()

