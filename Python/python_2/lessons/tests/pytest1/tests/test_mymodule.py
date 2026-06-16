# File: tests/test_mymodule.py

import pytest

def sum(a, b):
    return a + b

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    # TEST: Test fllito
    # assert sum(-1, 1) == 1

@pytest.fixture
def setup_dict():
    return {'a': 1, 'b': 2}

def test_keys(setup_dict):
    assert 'a' in setup_dict

def test_values(setup_dict):
    assert setup_dict['b'] == 2

@pytest.mark.parametrize(
    "input,expected",
    [
        (3, 9),
        (0, 0),
        (-2, 4),
    ]
)
def test_square(input, expected):
    assert input ** 2 == expected
