from utils import arrs
import pytest


@pytest.fixture
def value():
    return [1, 2, 3]


def test_get(value):
    assert arrs.get(value, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(value, -1, "test") == "test"
    assert arrs.get(value, 5, "test") == "test"


def test_slice(value):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(value, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(value) == value
    assert arrs.my_slice(value, 1, 10) == [2, 3]
