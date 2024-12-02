"""
    let compare test cases of 3 files test_<filename>.py
    with test_compare.py to have quick overview
    of which test cases failed
    to run it type in command line "pytest -v" 
"""
def test_greater():
    num = 100
    assert num == 100


def test_greater_equal():
    num = 100
    assert num >= 100


def test_less():
    num = 100
    assert num < 200
