from ply import lex, yacc
from errors import SyntaxAnomaly


class Compiler:
    # DO NOT DELETE
    tokens = (
        'LOCATIONQUERY',
        'NAMESPACE',
        'VARIABLEASSIGNMENT',
        'UNKNOWNPOSITION',
        'EXPLICITPOSITION',
        'POSITIONCHANGE',
        'EXISTINGREFERENCE',
        'NEWREFERENCE',
        'INLINECOMMENT',
        'MULTILINECOMMENT'
    )

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
    

    # Class methods
    def lexer(self, **kwargs):
        return lex.lex(module=self, **kwargs)

    def parser(self, **kwargs):
        return yacc.yacc(module=self, **kwargs)

    def __init__(self):
        pass

M = Compiler()
lexer = M.lexer()
parser = None #M.parser()

