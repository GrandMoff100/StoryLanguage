import os
from ply import yacc
from .tokens import tokens


DEV = os.getenv('MAINPYDEV')


# DOCS: https://ply.readthedocs.io/en/latest/ply.html#yacc

def p_value(p):
    '''place : NAMESPACE
             | variable
    value : NAMESPACE
          | GETMOSTRECENTVARIABLE
    variable : NAMESPACE
             | SETMOSTRECENTVARIABLE'''
    p[0] = p[1]


def p_assign_explicit_place(p):
    '''declaration : variable VARIABLEASSIGNMENT EXPLICITLOCATION place'''
    p[0] = None

def p_assign_unknown_place(p):
    '''declaration : variable VARIABLEASSIGNMENT UNKNOWNLOCATION'''
    p[0] = None


def p_error(p):
    print(p)


parser = yacc.yacc(write_tables=False, debug=DEV)
