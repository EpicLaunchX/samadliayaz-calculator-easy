from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main() -> None:
    calculator = Calculator()
    try:
        first_operand = int(input())
        second_operand = int(input())
        operand_name = input()
        operand = getattr(calculator, operand_name.strip(), None)

        first_operand = int(first_operand)
        second_operand = int(second_operand)
        if operand is None:
            raise ValueError(f"Unsupported operand type: {operand_name}")
    except ValueError:
        print(
            "Please enter two integer and one string operand (add, subtract, " "multiply or divide) by comma seperated. e.g.: 45, 35, add."
        )
    else:
        result = operand(operands_factory(first_operand, second_operand))
        print(result)


if __name__ == "__main__":
    main()
