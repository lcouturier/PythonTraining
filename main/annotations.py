import time

from dataclasses import dataclass


@dataclass(frozen=True)
class DurationResult:
    duration: float
    value: any


def memoize(f):
    """
    A decorator that caches the results of a function.

    The function passed to `memoize` should take a single argument.
    The return value of the function will be cached based on the argument.
    The cached values will be stored in a dictionary which is returned by the decorator.

    The decorator returns a new function which checks if the argument is in the cache.
    If the argument is in the cache, it returns the cached value.
    If the argument is not in the cache, it calls the original function with the argument,
    caches the return value, and returns the return value.

    Example:

    @memoize
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    fibonacci(10)  # This will be computed and cached.
    fibonacci(10)  # This will be retrieved from the cache.
    """
    cache = {}

    def inner(key):
        if key not in cache:
            cache[key] = f(key)
        return cache[key]

    return inner


def measure(f: callable):
    """
    Measures the execution time of a given function.

    Parameters
    ----------
    f : callable
        The function to be measured.

    Returns
    -------
    callable
        A function that takes one argument and returns a Result
        containing the execution time and the result of calling
        the original function with that argument.

    Examples
    --------
    @measure
    def slow_function(x: int) -> int:
        time.sleep(1)
        return x * x
    time_taken, result = slow_function(4)
    print(f"Execution time: {time_taken:.2f} seconds")
    print(f"Result: {result}")
    Execution time: 1.00 seconds

    Result: 16
    """

    def inner(value: any) -> DurationResult:
        start = time.time()
        result = f(value)
        end = time.time()
        return DurationResult(end - start, result)

    return inner


def log(f, withParams: bool = True, withReturn: bool = True):
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
        if withParams:
            print(f"Calling {f.__name__} with args={args} and kwargs={kwargs}")

        result = f(*args, **kwargs)
        if withReturn:
            print(f"{f.__name__} returned {result}")
        return result

    return inner
