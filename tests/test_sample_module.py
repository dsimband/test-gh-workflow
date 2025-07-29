import pytest
import sample_module


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
    ],
)
def test_add(a, b, expected):
    assert sample_module.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 4, 8),
        (-1, 3, -3),
        (0, 5, 0),
    ],
)
def test_multiply(a, b, expected):
    assert sample_module.multiply(a, b) == expected

