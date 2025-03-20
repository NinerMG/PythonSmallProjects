import pytest
"""Class to practice simple operations -by creating cypher coder and decoder with tests"""
def encrypt(originalText, shift):
    result = ""
    for char in originalText:
        if char.isalpha():
            shiftBase = ord('A') if char.isupper() else ord('a')
            result += chr(((ord(char) - shiftBase + shift) % 26 + shiftBase))
        else:
            result += char

    return  result

def decrypt(originalText, shift):
    return encrypt(originalText, -shift)


def test_basic_encryption():
    assert encrypt("ABC", 3) == "DEF"
    assert encrypt("xyz", 2) == "zab"


def test_basic_decryption():
    assert decrypt("DEF", 3) == "ABC"
    assert decrypt("zab", 2) == "xyz"

def test_case_sensitivity():
    assert encrypt("Hello", 5) == "Mjqqt"
    assert decrypt("Mjqqt", 5) == "Hello"

def test_case_sensitivity2():
    assert encrypt("Hello", 5) == "Mjqqt"
    assert decrypt("Mjqqt", 5) == "Hello"

def test_wrap_around():
    assert encrypt("XYZ", 3) == "ABC"
    assert encrypt("xyz", 3) == "abc"
    assert decrypt("ABC", 3) == "XYZ"

def test_special_characters():
    assert encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"

def test_large_shifts():
    assert encrypt("abc", 29) == "def"  # 29 ≡ 3 (mod 26)
    assert decrypt("def", 29) == "abc"

def test_zero_shift():
    assert encrypt("Hello", 0) == "Hello"
    assert decrypt("Hello", 0) == "Hello"
