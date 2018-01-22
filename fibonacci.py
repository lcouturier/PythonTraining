import utils


def fibonacci():
    while True:
        x, y = (0, 1)
        yield x
        yield y
        while True:
            x, y = x + y, x
            yield x


def getFibonacci(limit):
    items = []
    count = 0
    for i in fibonacci():
        items.append(i)
        count = count + 1
        if count == limit:
            break

    return items;


def fibonacci(n):
    if (n == 0): return 0
    if (n == 1): return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_by_cache():
    cache = {}

    def inner_fibonacci(key):
        if key not in cache:
            if (key == 0): return 0
            if (key == 1): return 1
            cache[key] = inner_fibonacci(key - 1) + inner_fibonacci(key - 2)
        return cache[key]

    return inner_fibonacci


def max_key_dictionary(d):
    return max(d, key=d.get)


def fibonacci_bottom_up():
    cache = {}
    cache[0] = 0
    cache[1] = 1

    def inner(key):
        if key in cache:
            return cache[key]
        max_key = max_key_dictionary(cache)
        for i in range(max_key + 1, key + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[key]

    return inner


def fibonacci_by_recurse_measure():
    return utils.measure(fibonacci)


def fibonacci_by_memoize_measure():
    return utils.measure(fibonacci_by_cache())

def fibonacci_by_cache_measure():
    return utils.measure(fibonacci_bottom_up())


def main():
    f2 = fibonacci_by_memoize_measure()
    result = f2(100)
    print(result)

    result = f2(10)
    print(result)

    f3 = fibonacci_by_cache_measure()
    result = f3(100)
    print(result)

    result = f3(10)
    print(result)


if __name__ == '__main__':
    main()
