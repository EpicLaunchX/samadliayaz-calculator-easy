from src.pytemplate import Operands, operands_factory


def test_value():
    obj = Operands(1, 2)
    assert obj.first_operand == 1
    assert obj.second_operand == 2


def test_type():
    obj = Operands(1, 2)
    assert isinstance(obj.first_operand, int)
    assert isinstance(obj.second_operand, int)


def test_operands_factory():
    x = operands_factory(1, 2)
    assert isinstance(x, Operands)
    assert x.first_operand == 1
    assert x.second_operand == 2
