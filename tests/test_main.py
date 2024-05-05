from unittest.mock import patch

import pytest

from src.pytemplate import main


@pytest.mark.parametrize("input, output", [
    ("45, 35, add", 80),
    ("45, 35, subtract", 10),
    ("3, 5, multiply", 15),
    ("5, 2, divide", 2),
    ("1 2 add", None),
    ("one, 2, add", None),
    ("1, 2, mult", None)
])
def test_main_success(input, output):
    with patch('builtins.input', return_value=input):
        result = main()
        assert result == output
