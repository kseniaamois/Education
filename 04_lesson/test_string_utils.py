import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# --- Тесты для capitalize ---

@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
        ("a", "A"),
        ("1abc", "1abc"),
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", "   "),
        ("123abc", "123abc"),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

def test_capitalize_none_raises():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

# --- Тесты для trim ---

@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("  hello", "hello"),
        ("no_spaces", "no_spaces"),
        ("   multiple   spaces   ", "multiple   spaces   "),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("    ", ""),
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

def test_trim_none_raises():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

# --- Тесты для contains ---

@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "S"),
        ("hello world", " "),
        ("12345", "3"),
        ("test", "t"),
    ],
)
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True

@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "U"),
        ("hello", "z"),
        ("", "a"),
    ],
)
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False

def test_contains_none_raises():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")

# --- Тесты для delete_symbol ---

@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("hello world", "l", "heo word"),
        ("aaaaaa", "a", ""),
        ("abcabcabc", "b", "acacac"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "z", "SkyPro"),
        ("", "a", ""),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

def test_delete_symbol_none_raises():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
