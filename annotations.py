from functools import wraps
from threading import Lock
import time
from collections import namedtuple
from typing import Any, Callable, OrderedDict

Result = namedtuple("Result", ["duration", "value"])


class composable:
    def __init__(self, f):
        self.f = f

    def __rshift__(self, other):
        return composable(lambda x: other.f(self.f(x)))

    def __call__(self, x):
        return self.f(x)


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


def my_lru_cache(max_size: int) -> Callable:
    cache: OrderedDict[str, Any] = OrderedDict[str, Any]()
    lock = Lock()

    def decorator(f: Callable) -> Callable:
        def inner(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            with lock:
                if key in cache:
                    return cache[key]
            result = f(*args, **kwargs)
            with lock:
                cache[key] = result
                if len(cache) > max_size:
                    # Supprime le plus ancien élément du cache (la clé insérée en premier), pour respecter la taille maximale du cache LRU.
                    cache.popitem(last=False)
            return result

        return inner

    return decorator
