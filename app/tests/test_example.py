import pytest

# Replacing String with another string
def test_strReplace():
    string = "Hello, World!"
    assert string.replace("H", "J") == "Jello, World!"
# String Split - Splits a string to two substrings
def test_strSplit():
    string = "Hello,World"
    assert string.split(",") == ["Hello", "World"]
# String Strip
def test_strStrip():
    string = " Hello, World! "
    assert string.strip() == "Hello, World!"
# String Concatenate
def test_strConcat():
    string1 = "Hello"
    string2 = "World"
    assert string1 + string2 == "HelloWorld"
