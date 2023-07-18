import pytest
from main import evaluate_expression


def test_valid_expression():
    assert evaluate_expression("2 + 3") == 5


def test_invalid_syntax():
    assert evaluate_expression("2 +") == "Error: invalid syntax"


def test_invalid_variable():
    assert evaluate_expression("x + 5") == "Error: invalid variable or function name"


def test_division_by_zero():
    assert evaluate_expression("10 / 0") == "Error: division by zero"


def test_other_exceptions():
    assert evaluate_expression("2 / 'a'") == "Error: unsupported operand type(s) for /: 'int' and 'str'"
