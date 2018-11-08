import pytest
from baseball_qualifying_offer.import_data import fetch_html

# size
url = 'https://questionnaire-148920.appspot.com/swe/data.html'
def f1 ():
    return fetch_html(url)

def test_f1 ():
    assert len(f1()) > 0

# def test_f1_2 ():
#     assert type(f1()[0]) is str
# def f2 ():
#     return vectorize(get_doc(size), '')
# def test_f2 ():
#     assert type(f2()) is numpy.ndarray