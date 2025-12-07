import itertools as it
import math
import random
from typing import Callable, Iterator


def measure(f: Callable) -> Callable:
    """
    Measures the execution time of the given function 'f' when called, and prints the elapsed time.

    Returns a wrapper function that, when called, executes 'f' with the provided arguments,
    times the execution duration, prints the elapsed time, and returns the result.
    """
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Elapsed: {end - start:.8f} seconds")
        return result

    return wrapper


def load_lines(filename: str) -> Iterator[str]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            yield from (line.rstrip("\n") for line in f)
    except Exception as e:
        print(f"Could not open file '{filename}': {e}")
        return


def random_by_seq() -> Iterator[int]:
    x = 1
    while True:
        yield x
        x = x + random.randint(1, 100)


def run_random(limit: int) -> None:
    for i in random_by_seq():
        if i > limit:
            break
        print(i)


def unfold[T](v: T, f: Callable[[T], T]) -> Iterator[T]:
    yield v
    while True:
        v = f(v)
        yield v


def loop(limit: int) -> None:
    for i in it.takewhile(lambda x: x < limit, unfold(1, lambda x: x + 1)):
        print("%.2d" % i)


def is_prime(value: int) -> bool:
    """Return True if value is a prime number, else False.

    Uses 6k ± 1 optimization. Handles edge cases and small numbers first,
    then skips redundant checks. Avoids unnecessary variable assignment,
    and limits scope of variables.
    """
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    limit = int(math.isqrt(value))
    for i in range(5, limit + 1, 6):
        if value % i == 0 or value % (i + 2) == 0:
            return False
    return True


def primes() -> Iterator[int]:
    yield 2
    yield 3
    x = 5
    while True:
        if is_prime(x):
            yield x
        x = x + 2


def main():
    for index, _ in enumerate(["apple", "banana", "cherry"]):
        print(index)
