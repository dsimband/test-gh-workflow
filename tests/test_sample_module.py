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
        (3, 2, 1),
        (0, 5, -5),
        (-1, -1, 0),
    ],
)
def test_subtract(a, b, expected):
    assert sample_module.subtract(a, b) == expected


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


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 2, 2.0),
        (-3, -3, 1.0),
        (5, 2, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert sample_module.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError):
        sample_module.divide(1, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (3, 2, 9),
    ],
)
def test_power(a, b, expected):
    assert sample_module.power(a, b) == expected
