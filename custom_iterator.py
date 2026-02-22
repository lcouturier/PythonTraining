class EvenNumbers:
    n: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x


class Factorial:
    value: int = 1
    index: int = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.value *= self.index
        self.index += 1
        return self.value


class fibonacci_iter:
    (a, b) = (0, 1)

    def __iter__(self):
        return self

    def __next__(self) -> int:
        value = self.a
        (self.a, self.b) = (self.b, self.a + self.b)
        return value


class Chunked:
    size: int = 0

    def __init__(self, iterable, size: int):
        self.iterable = iter(iterable)
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):

        chunk: list[int] = []
        for _ in range(self.size):
            chunk.append(next(self.iterable))
        return chunk


class PairWise:
    prev: int | None = None
    next: int = 0

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.prev = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.prev is None:
            self.prev = next(self.iterable)
            self.next = next(self.iterable)
            return self.prev, self.next
        else:
            self.prev = self.next
            self.next = next(self.iterable)
            return self.prev, self.next


if __name__ == "__main__":
    for i in PairWise(range(100)):
        print(i)
