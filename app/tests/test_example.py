"""Provides some default tests functions."""


def test_strreplace():
    """Replacing String with another string."""
    string = "Hello, World!"
    assert string.replace("H", "J") == "Jello, World!"


def test_strsplit():
    """String Split - Splits a string to two substrings."""
    string = "Hello,World"
    assert string.split(",") == ["Hello", "World"]


def test_strstrip():
    """String Strip."""
    string = " Hello, World! "
    assert string.strip() == "Hello, World!"


def test_strconcat():
    """String Concatenate."""
    string1 = "Hello"
    string2 = "World"
    assert string1 + string2 == "HelloWorld"
