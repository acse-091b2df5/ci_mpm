from functools import cache

__all__ = ['my_sum', 'factorial', 'sin', 'say_best_player']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


@cache
def sin(x):
    sin_x = 0
    n_max = 100
    for n in range(n_max):
        sin_x += (-1)**(n)/factorial(2*n+1)*x**(2*n+1)
    return sin_x


@cache
def say_best_player(player):
    output = player == 'Messi' or player == 'messi'
    return output

