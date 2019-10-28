import pytest
from .chuck import joke_category, joke_search


def test_joke_category_valid_category():
    result = joke_category('science')
    assert result is not None
    assert len(result) > 0


def test_joke_category_invalid_category():
    result = joke_category('not a category')
    assert result is None


def test_joke_search_result_found():
    result = joke_search('paradox')
    assert result is not None
    assert len(result) > 0


def test_joke_search_result_not_found():
    result = joke_search('this string is not found in the joke database')
    assert result is None
