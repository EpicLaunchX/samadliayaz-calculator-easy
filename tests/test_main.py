from unittest.mock import patch

from src.pytemplate import main


def test_add(capsys):
    with patch("builtins.input", side_effect=[45, 35, "add"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == "80\n"

def test_subtract(capsys):
    with patch("builtins.input", side_effect=[45, 35, "subtract"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == "10\n"

def test_multiply(capsys):
    with patch("builtins.input", side_effect=[3, 5, "multiply"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == "15\n"

def test_divide(capsys):
    with patch("builtins.input", side_effect=[5, 2, "divide"]):
        main()
        captured = capsys.readouterr()
        assert captured.out == "2\n"
