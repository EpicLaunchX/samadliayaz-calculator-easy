import pytest

from src.pytemplate import Calculator, operands_factory


def test_add():
    assert Calculator().add(operands_factory(45, 35)) == 80


def test_subtract():
    assert Calculator().subtract(operands_factory(45, 35)) == 10


def test_multiply():
    assert Calculator().multiply(operands_factory(3, 5)) == 15


def test_divide():
    assert Calculator().divide(operands_factory(6, 2)) == 3
    assert Calculator().divide(operands_factory(5, 2)) == 2
    with pytest.raises(ValueError) as excinfo:
        Calculator().divide(operands_factory(5, 0))
    assert "Cannot divide by zero" in str(excinfo.value)
