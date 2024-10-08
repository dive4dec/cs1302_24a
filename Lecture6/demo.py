"""
Demo
====

This module provides a demonstration of using decorators for caching and logging function calls.
"""
from .recurtools import caching, print_function_call  # relative import

# main script
if __name__ == "__main__":
    @caching
    @print_function_call
    def fibonacci(n):
        """Returns the Fibonacci number of order n."""
        return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0

    fibonacci(5)
    fibonacci(5)
    fibonacci.cache_clear()
    fibonacci(5)
