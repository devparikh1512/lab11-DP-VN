# https://github.com/devparikh1512/lab11-DP-VN
# Partner 1: Dev Parikh
# Partner 2: Vishal Naveen
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("cannot take the square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("invalid base or argument")
    return math.log(b, a)

def exp(a, b):
    return a ** b
