import sys


class BaseError:
    def __init__(self, *args):
        self.args = [str(x) for x in args]
    
    def run(self):
        print('\n')
        print(
            self.__class__.__name__,
            ', '.join(self.args),
            sep=': '
        )
        sys.exit(3)


class SyntaxAnomaly(BaseError):
    pass