import pytest
from baseball_qualifying_offer.calculate_offer import avg_best125

def f1 (num_list):
    return avg_best125(num_list)

def test_f1 ():
    l = [i for i in range(-126, 126)]
    assert f1(l) == (1 + 125) / 2

def test_f2 ():
    l = [i for i in range(1, 11)]
    assert f1(l) == (1 + 10) / 2