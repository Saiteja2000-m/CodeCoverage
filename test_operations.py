# math_operations_test.py

# Code: Math Operations Functions
def square(x):
    return x * x

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Tests
def test_square():
    assert square(4) == 16

def test_factorial():
    assert factorial(5) == 120

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(0) == 0
