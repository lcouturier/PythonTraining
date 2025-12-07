from annotations import cache
import utils


@cache
def fibonacci_cached(n: int) -> int:
    """Returns the nth Fibonacci number using cache decorator."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


def get_fibonacci(limit: int) -> list[int]:
    items: list[int] = []
    count = 0
    for i in fibonacci():
        items.append(i)
        count = count + 1
        if count == limit:
            break

    return items


def fibonacci_first(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_by_cache():
    cache = {}

    def inner_fibonacci(key):
        if key not in cache:
            if key == 0:
                return 0
            if key == 1:
                return 1
            cache[key] = inner_fibonacci(key - 1) + inner_fibonacci(key - 2)
        return cache[key]

    return inner_fibonacci


def max_key_dictionary(d):
    return max(d, key=d.get)


def fibonacci_bottom_up():
    cache = {0: 0, 1: 1}

    def inner(key):
        if key in cache:
            return cache[key]
        max_key = max_key_dictionary(cache)
        for i in range(max_key + 1, key + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[key]

    return inner


@cache
def fibonacci_by_recurse_measure():
    return utils.measure(fibonacci)


def fibonacci_by_memoize_measure():
    return utils.measure(fibonacci_by_cache())


def fibonacci_by_cache_measure():
    return utils.measure(fibonacci_bottom_up())


def main():
    f2 = fibonacci_by_recurse_measure()
    result = f2(100)
    print(result)

    result = f2(100)
    print(result)


if __name__ == "__main__":
    main()
