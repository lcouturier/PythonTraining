import itertools as it
import time


def factorialCore():
    x, y = (1, 1)
    yield x
    while (True):
        x, y = (x * y, y + 1)
        yield x


def factorialCore2(limit):
    for i in it.takewhile(lambda x: x < limit, factorialCore()):
        yield i


def factorial(limit):
    for i in factorialCore2(limit):
        print(i)


def fibonacci():
    while (True):
        x, y = (0, 1)
        yield x
        yield y
        while True:
            x, y = x + y, x
            yield x


def fibonacci(n):
    if (n == 0): return 0
    if (n == 1): return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


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


def unfold(v, f):
    yield v
    while True:
        v = f(v)
        yield v


def loop(limit):
    for i in it.takewhile(lambda x: x < limit, unfold(1, lambda x: x + 1)):
        print('%.2d' % i)
