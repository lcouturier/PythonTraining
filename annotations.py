from functools import wraps
import time
from collections import namedtuple
from typing import Any, Callable

Result = namedtuple("Result", ["duration", "value"])


def measure(f: Callable[[Any], Any]) -> Callable[[Any], Result]:
    """
    Decorator to measure the execution time of a function taking a single argument.

    Returns a function that, given an argument, returns a Result(duration, value).
    """

    @wraps(f)
    def inner(arg: Any) -> Result:
        start = time.time()
        value = f(arg)
        duration = time.time() - start
        return Result(duration, value)

    return inner


def log(f):
    """
    A decorator that logs the arguments and return value of a function.

    Parameters
    ----------
    f : callable
        The function to be logged.

    Returns
    -------
    callable
        A function that takes arbitrary arguments and keyword arguments
        and returns the result of calling the original function with
        those arguments and keyword arguments.

    Examples
    --------
    @log
    def add(a, b):
        return a + b
    result = add(3, 4)
    print(f"Result: {result}")
    Result: 7
    """

    def inner(*args, **kwargs):
        print(f"Calling {f.__name__} with args={args} and kwargs={kwargs}")
        result = f(*args, **kwargs)
        print(f"{f.__name__} returned {result}")
        return result

    return inner


def cache(f: Callable) -> Callable:
    """
    A decorator that caches the results of the decorated function
    based on its arguments. Prevents redundant computations by using
    a dictionary keyed by argument tuples.
    example:

    @cache
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    """
    cache_dict = {}

    @wraps(f)
    def inner(*args, **kwargs):
        # Use a tuple of args and frozenset of kwargs as the dictionary key for safety and hashability
        key = (args, frozenset(kwargs.items()))
        if key not in cache_dict:
            cache_dict[key] = f(*args, **kwargs)
        return cache_dict[key]

    return inner
