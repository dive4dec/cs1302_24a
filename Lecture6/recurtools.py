'''
Recursion Tools
===============

Contain tools to print the call stack and cache the return values
of a recursive function.
'''

import functools


def _argument_string(*args, **kwargs):
    """Return the string representation of the list of arguments."""
    return "({})".format(
        ', '.join(
            [
                *[f'{v!r}' for v in args],  # arguments
                *[
                    f'{k}={v!r}' for k, v in kwargs.items()
                ],  # keyword arguments
            ]
        )
    )


def print_function_call(f):
    """Decorate a recursive function to print the call stack.

    The decorator also keep tracks of the number and depth of a recursive call.

    Parameters
    ----------
    f: Callable
        A recursive function.

    Returns
    -------
    Callable:
        The decorated function that also prints the function call
        when called.

    Examples
    --------
    >>> @print_function_call
    ... def fibonacci(n):
    ...     return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0
    ...
    >>> fibonacci(5)
      1:fibonacci(5)
      2:|fibonacci(4)
      3:||fibonacci(3)
      4:|||fibonacci(2)
      5:||||fibonacci(1)
      6:||||fibonacci(0)
      7:|||fibonacci(1)
      8:||fibonacci(2)
      9:|||fibonacci(1)
     10:|||fibonacci(0)
     11:|fibonacci(3)
     12:||fibonacci(2)
     13:|||fibonacci(1)
     14:|||fibonacci(0)
     15:||fibonacci(1)
    Done
    5
    """

    @functools.wraps(f)  # give wrapper the identity of f and more
    def wrapper(*args, **kwargs):
        nonlocal count, depth
        count += 1
        depth += 1
        call = f"{f.__name__}{_argument_string(*args, **kwargs)}"
        print(f"{count:>3}:{'|' * depth}{call}")

        value = f(*args, **kwargs)  # calls f

        depth -= 1
        if depth == -1:
            print("Done")
            count = 0
        return value

    count, depth = 0, -1
    return wrapper  # return the decorated function


def caching(f):
    """Cache the return value of a function that takes a single argument.

    Parameters
    ----------
    f: Callable
        A function that takes a single argument.

    Returns
    -------
    Callable:
        The function same as f but has its return valued automatically cached
        when called. It has a method clear_cache to clear its cache.

    Examples
    --------
    >>> @print_function_call
    ... @caching
    ... def fibonacci(n):
    ...     return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0
    ...
    >>> fibonacci(5)
      1:fibonacci(5)
      2:|fibonacci(4)
      3:||fibonacci(3)
      4:|||fibonacci(2)
      5:||||fibonacci(1)
      6:||||fibonacci(0)
      7:|||fibonacci(1)
    read from cache
      8:||fibonacci(2)
    read from cache
      9:|fibonacci(3)
    read from cache
    Done
    5
    >>> fibonacci(5)
      1:fibonacci(5)
    read from cache
    Done
    5
    >>> fibonacci.clear_cache()
    >>> fibonacci(5)
      1:fibonacci(5)
      2:|fibonacci(4)
      3:||fibonacci(3)
      4:|||fibonacci(2)
      5:||||fibonacci(1)
      6:||||fibonacci(0)
      7:|||fibonacci(1)
    read from cache
      8:||fibonacci(2)
    read from cache
      9:|fibonacci(3)
    read from cache
    Done
    5
    """

    @functools.wraps(f)
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        else:
            print("read from cache")
        return cache[n]

    cache = {}
    wrapper.cache_clear = lambda: cache.clear()  # add method to clear cache
    return wrapper
