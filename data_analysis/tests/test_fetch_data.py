import pytest
from baseball_qualifying_offer.import_data import fetch_html
from baseball_qualifying_offer.import_data import parse_int
from baseball_qualifying_offer.import_data import parse_salaries

# fetch_html tests
url = 'https://questionnaire-148920.appspot.com/swe/data.html'

def f1 ():
    return fetch_html(url)

def test_f1 ():
    assert len(f1()) > 0

# parse_int tests
def f2 (str):
    return parse_int(str)

def test_f2_1 ():
    str = '$50,000,000'
    assert f2(str) == 50000000

def test_f2_2 ():
    str = '$$$50,000,'
    assert f2(str) == 50000

def test_f2_3 ():
    str = '$50,000,000'
    assert f2(str) == 50000000

def test_f2_4 ():
    try:
        str = 'no salary data'
        f2(str)
        assert False
    except ValueError:
        assert True

def test_f2_5 ():
    try:
        str = ''
        f2(str)
        assert False
    except ValueError:
        assert True

# fetch_salaries test
def f3 (s_list):
    return parse_salaries(s_list)

def test_f3 ():
    s_list = ['$24,000,000', '$987,500', '','$4,500,000', '$507,500', '$507,500', 'no salary data', '$$$507,500']
    assert f3(s_list) == [24000000, 987500, 4500000, 507500, 507500, 507500]