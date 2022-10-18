import pytest
import numpy as np

from simple_functions import my_sum, factorial, sin, say_best_player


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('x, expected', [
        (np.pi/2, 1),
        (np.pi, 0),
        (np.pi/4, np.sqrt(2)/2)
    ])
    def test_sin(self, x, expected):
        '''Test our sin function'''
        answer = sin(x)
        assert np.isclose(answer, expected)

    @pytest.mark.parametrize('player, expected', [
        ('Ronaldo', False),
        ('Messi', True)
    ])
    def test_player(self, player, expected):
        '''Test our player function'''
        answer = say_best_player(player)
        assert answer == expected

