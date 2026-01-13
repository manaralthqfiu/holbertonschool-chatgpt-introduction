#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a number using recursion.

    Parameters:
        n (int): The number to compute the factorial for. 
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
