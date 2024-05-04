from unittest.mock import patch

import pytest

from src.pytemplate import main


@pytest.mark.parametrize("input, output", [
    ("45, 35, add", 80),
    ("45, 35, subtract", 10),
    ("3, 5, multiply", 15),
    ("5, 2, divide", 2),
])
def test_main_success(input, output):
    with patch('builtins.input', return_value=input):
        result = main()
        assert result == output


@pytest.mark.parametrize("input, exception", [
    ("1 2 add", ValueError),
    ("one, 2, add", ValueError),
    ("1, 2, mult", ValueError)
])
def test_main_failure(input, exception):
    with patch('builtins.input', return_value=input):
        exception_message = (
            "Please enter two integer and one string operand (add, subtract, "
            "multiply or divide) by comma seperated. e.g.: 45, 35, add. ")
        with pytest.raises(exception) as exc_info:
            main()
        assert exception_message in str(exc_info.value)
