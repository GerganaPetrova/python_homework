from itertools import cycle

def alternate(*args):
    return (next(argument) for argument in cycle([arg() for arg in args]))
