from typing import Optional

from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main() -> Optional[int]:
    calculator = Calculator()
    try:
        op1, op2, op_name = input().split(",")
        operand = getattr(calculator, op_name.strip(), None)

        op1 = int(op1)
        op2 = int(op2)
        if operand is None:
            raise ValueError(f"Unsupported operand type: {op_name}")
    except ValueError:
        print(
            "Please enter two integer and one string operand (add, subtract, " "multiply or divide) by comma seperated. e.g.: 45, 35, add. "
        )
        return None
    return operand(operands_factory(op1, op2))


if __name__ == "__main__":
    main()
