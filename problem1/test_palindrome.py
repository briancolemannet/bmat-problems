import pytest
from .palindrome import is_palindrome


@pytest.mark.parametrize("test_input,expected", [
    (1, True),
    (22, True),
    (333, True),
    (313, True),
    (627, False),
    (9876789, True),
    (9846789, False),
    (987789, True),
    (967789, False),
    (-1, False)
])
def test_is_palindrome(test_input: int, expected: bool):
    assert is_palindrome(test_input) == expected
