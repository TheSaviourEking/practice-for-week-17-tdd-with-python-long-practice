import pytest
from app.roman_numerals import parse

def test_roman_numeral_parser():
    # Arrange
    value = parse('IX')
    # Assert
    assert value == 9
