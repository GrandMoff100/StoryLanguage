import os
import sys
import click
from compiler import parser, lexer


@click.command()
@click.argument('filepath', required=True)
@click.option('-v', '--verbose', default=True)
def cli(filepath, verbose):
    with open(filepath, 'r') as f:
        read = f.read()
    
    """
    if verbose:
        click.echo('Showing tokens...')
    lexer.input(read)
    for tok in lexer:
        click.echo(tok)
    """
    if verbose:
        click.echo('Showing parse...')
    click.echo(parser.parse(read))
        

if __name__ == '__main__':
    if os.getenv('MAINPYDEV'):
        sys.argv += ['directions.txt']
    cli()

