from annotations import cache
from utils import measure


@cache
def fibonacci_cached(n: int) -> int:
    """Returns the nth Fibonacci number using cache decorator."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci(limit: int) -> list[int]:
    items: list[int] = []
    count = 0
    for i in fibonacci():
        items.append(i)
        count = count + 1
        if count == limit:
            break

    return items


def max_key_dictionary(d):
    return max(d, key=d.get)


def fibonacci_top_down():
    """
    Returns the nth Fibonacci number using a top-down approach and cache.

    The function starts with an empty cache and recursively calculates the Fibonacci
    numbers from the top down. The intermediate Fibonacci numbers are cached for
    later use.

    This approach has a time complexity of O(n) and a space complexity of O(n).
    """
    cache = {}

    def inner(key):
        if key in cache:
            return cache[key]
        if key == 0:
            return 0
        if key == 1:
            return 1
        cache[key] = inner(key - 1) + inner(key - 2)
        return cache[key]

    return inner


def fibonacci_bottom_up():
    """
    Returns the nth Fibonacci number using a bottom-up approach and cache.

    The function starts with a cache containing the Fibonacci numbers for 0 and 1.
    It then iterates from the last cached Fibonacci number to the nth Fibonacci number.
    The intermediate Fibonacci numbers are calculated and cached for later use.

    This approach has a time complexity of O(n) and a space complexity of O(n).
    """
    cache = {0: 0, 1: 1}

    def inner(key):
        if key in cache:
            return cache[key]
        max_key = max_key_dictionary(cache)
        for i in range(max_key + 1, key + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[key]

    return inner


def main():
    f2 = measure(fibonacci_bottom_up())  # fibonacci_top_down()
    result = f2(100)
    print(result)

    result = f2(100)
    print(result)


if __name__ == "__main__":
    main()
