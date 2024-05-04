from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int):
    return Operands(first_operand, second_operand)
