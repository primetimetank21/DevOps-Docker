"""Docstring for test_say_my_name.py """
from io import StringIO
from mock import patch
from .say_name import say_my_name


@patch("sys.stdout", new_callable=StringIO)
def test_say_my_name(mock_stdout):
    """Tests say_my_name() function"""
    names = ["John", "Mary", "Quincy"]

    for name in names:
        say_my_name(name)
        assert mock_stdout.getvalue().strip() == f"Hello {name}!"
        mock_stdout.truncate()
        mock_stdout.seek(0)
