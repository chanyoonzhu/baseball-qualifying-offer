import pytest
import random
from baseball_qualifying_offer.calculate_offer import *

def f1 (num_list):
    return avg_salary(num_list)

def test_f1 ():
    l = [i for i in range(1, 126)]
    assert f1(l) == (1 + 125) / 2

def test_f2 ():
    l = [i for i in range(1, 11)]
    assert f1(l) == (1 + 10) / 2

def f2 (data, limit):
    return calc_qualifying_offer(data, limit)

def test_f2_1():
    limit = 100
    data, answer = [], []
    for x in range(500,0,-2):
        data.append(['name', x])
        answer.append(['name', x])
    random.shuffle(data)
    data.insert(0, ['col1', 'col2'])
    answer.insert(0, ['col1', 'col2'])
    assert f2(data, limit) == (answer[limit][1] + answer[1][1]) / 2

def f3 (data, limit):
    return best_to_range(data, limit)

def test_f3_1():
    limit = 10
    data, answer = [], []
    for x in range(20,0,-1):
        data.append(['name', x])
        answer.append(['name', x])
    random.shuffle(data)
    data.insert(0, ['col1', 'col2'])
    answer.insert(0, ['col1', 'col2'])
    assert f3(data, limit) == answer[:limit+1]
        