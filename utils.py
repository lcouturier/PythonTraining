import itertools as it
import math
import random
from typing import Iterator


def load_lines(filename: str) -> Iterator[str]:
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.rstrip('\n')
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return iter([])


def map_index(items) -> Iterator[tuple[int, any]]:
    return enumerate(items)


def random_by_seq():
    x = 1
    while True:
        yield x
        x = x + random.randint(1, 100)


def run_random(limit):
    for i in random_by_seq():
        if i > limit:
            break
        print(i)


def unfold(v, f):
    yield v
    while True:
        v = f(v)
        yield v


def loop(limit):
    for i in it.takewhile(lambda x: x < limit, unfold(1, lambda x: x + 1)):
        print('%.2d' % i)


def is_prime(value):
    if value < 2:
        return False
    if value == 2 or value == 3:
        return True
    if value % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):  # only odd numbers
        if value % i == 0:
            return False
    return True


def primes():
    yield 2
    yield 3
    x = 5
    while True:
        if is_prime(x):
            yield x
        x = x + 2


def main():
    for (index, item) in map_index(["apple", "banana", "cherry"]):
        print(index)
