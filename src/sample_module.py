"""Sample module for integration testing.

This module provides simple math utilities that are used by the test suite.
"""


def add(a: int, b: int) -> int:
    """Return sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of ``a`` and ``b``."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return product of ``a`` and ``b``."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return quotient of ``a`` and ``b``."""
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b


def power(a: int, b: int) -> int:
    """Return ``a`` raised to the power of ``b``."""
    return a**b
