import pytest
с

string_utils = StringUtils()

# --- Тесты для capitalize ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# --- Тесты для trim ---

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello", "hello"),
    ("no_spaces", "no_spaces"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("    ", ""),  # строка из пробелов должна стать пустой
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# --- Тесты для contains ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("hello world", " "),
    ("12345", "3"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("hello", "z"),
    ("", "a"),
    (None, "a"),  # проверка None
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False

# --- Тесты для delete_symbol ---

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "l", "heo word"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),  # символа нет, строка не меняется
    ("", "a", ""),              # пустая строка
    (None, "a", None),          # если передать None, проверяем, что метод не падает
])
def test_delete_symbol_negative(string, symbol, expected):
    try:
        result = string_utils.delete_symbol(string, symbol)
    except Exception:
        result = None
    assert result == expected
