import itertools as it


def factorial(value):
    if value == 1:
        return value
    else:
        return value * factorial(value - 1)


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
