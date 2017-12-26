import utils


def fibonacci():
    while (True):
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
        if (count == limit):
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


def fibonacci_by_cache_measure():
    return utils.measure(fibonacci_by_cache())


def main():
    f = fibonacci_by_cache_measure()
    result = f(20)
    print(result)

    result = f(10)
    print(result)


if __name__ == '__main__':
    main()
