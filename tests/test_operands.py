from src.pytemplate import Operands


def test_value():
    obj = Operands(1, 2)
    assert obj.first_operand == 1
    assert obj.second_operand == 2


def test_type():
    obj = Operands(1, 2)
    assert isinstance(obj.first_operand, int)
    assert isinstance(obj.second_operand, int)
