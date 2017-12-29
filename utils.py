import itertools as it
import math
import random
import time


def memoize(f):
    cache = {}

    def inner(key):
        if key not in cache:
            cache[key] = f(key)
        return cache[key]

    return inner

def measure(f):
    def inner(value):
        start = time.time()
        result = f(value)
        end = time.time()
        return end - start, result

    return inner


def random_by_seq():
    x = 1
    while True:
        yield x;
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


def isPrime(value):
    if value < 2: return False
    if value == 2 or value == 3: return True
    if value % 2 == 0: return False
    for i in range(2, int(math.sqrt(value)) + 1):  # only odd numbers
        if value % i == 0:
            return False
    return True


def primes():
    yield 2;
    yield 3;
    x = 5
    while True:
        if isPrime(x):
            yield x;
        x = x + 2
