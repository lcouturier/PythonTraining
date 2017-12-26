import itertools as it
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


def unfold(v, f):
    yield v
    while True:
        v = f(v)
        yield v


def loop(limit):
    for i in it.takewhile(lambda x: x < limit, unfold(1, lambda x: x + 1)):
        print('%.2d' % i)
