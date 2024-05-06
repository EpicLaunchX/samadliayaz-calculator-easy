from unittest.mock import patch

import pytest

from src.pytemplate import main


@pytest.mark.parametrize(
    "input, output",
    [
        ("45, 35, add", "80\n"),
        ("45, 35, subtract", "10\n"),
        ("3, 5, multiply", "15\n"),
        ("5, 2, divide", "2\n"),
        (
            "1 2 add",
            "Please enter two integer and one string operand (add, subtract, "
            "multiply or divide) by comma seperated. e.g.: 45, 35, add.\n",
        ),
        (
            "one, 2, add",
            "Please enter two integer and one string operand (add, subtract, "
            "multiply or divide) by comma seperated. e.g.: 45, 35, add.\n",
        ),
        (
            "1, 2, mult",
            "Please enter two integer and one string operand (add, subtract, "
            "multiply or divide) by comma seperated. e.g.: 45, 35, add.\n",
        ),
    ],
)
def test_main(input, output, capsys):
    with patch("builtins.input", return_value=input):
        main()
        captured = capsys.readouterr()
        assert captured.out == output
