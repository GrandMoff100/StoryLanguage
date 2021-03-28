import os
import sys
import click
from compiler import parser, lexer


@click.command()
@click.argument('filepath', required=True)
def cli(filepath):
    with open(filepath, 'r') as f:
        read = f.read()
    
    lexer.input(read)
    for tok in lexer:
        print(tok)
    

if __name__ == '__main__':
    if os.getenv('MAINPYDEV'):
        sys.argv += ['directions.txt']
    cli()

