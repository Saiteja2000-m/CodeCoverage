# string_utils_test.py

# Code: String Utilities Functions
def capitalize_first_letter(s):
    if not s:
        return ''
    return s[0].upper() + s[1:]

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]


# Tests
def test_capitalize_first_letter():
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("") == ""

def test_reverse_string():
    assert reverse_string("abcd") == "dcba"

def test_is_palindrome():
    assert is_palindrome("madam") is True
    assert is_palindrome("hello") is False
