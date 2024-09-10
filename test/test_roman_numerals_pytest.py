import pytest
from pytest import mark
from app.roman_numerals import parse

@mark.parametrize('s, expected', [("IX", 9)])
def test_roman_numeral_parser(s, expected):
    # Arrange
    value = parse(s)
    # Assert
    assert value == expected
