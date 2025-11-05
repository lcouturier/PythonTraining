import itertools as it


def factorial_by_seq():
    (x, y) = (1, 1)
    while True:
        yield x
        (x, y) = (x * y, y + 1)


def factorial(value):
    if value == 1:
        return value
    return value * factorial(value - 1)


def factorial_by_acc(value):
    def util(x, acc):
        if x == 0:
            return acc
        else:
            return util(x - 1, acc * x)

    return util(value, 1)


def generate_factorial(limit):
    def generate():
        x, y = (1, 1)
        yield x
        while True:
            x, y = (x * y, y + 1)
            yield x

    for i in it.takewhile(lambda x: x < limit, generate()):
        yield i


def factorial(limit):
    for i in generate_factorial(limit):
        print(i)


def max_key_dictionary(d):
    return max(d, key=d.get)


def factorial_bottom_up():
    cache = {0: 1}

    def inner(key):
        if key in cache:
            return cache[key]
        max_key = max_key_dictionary(cache)
        for i in range(max_key + 1, key + 1):
            cache[i] = cache[i - 1] * i

        return cache[key]

    return inner


def main():
    f = factorial_bottom_up()
    result = f(10)
    print(result)
    result = f(11)
    print(result)


if __name__ == '__main__':
    main()
