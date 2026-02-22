from typing import Callable, Iterable, Iterator, List


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

    def __next__(self) -> list[int]:
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


class LeftJoin[L, R, K]:
    left: Iterator[L]
    left_key: Callable[[L], K]
    right_key: Callable[[R], K]
    right_dict: dict[K, List[R]]

    def __init__(
        self,
        left: Iterable[L],
        right: Iterable[R],
        left_key: Callable[[L], K],
        right_key: Callable[[R], K],
    ) -> None:
        self.left = iter(left)
        self.left_key = left_key
        self.right_key = right_key
        self.right_dict: dict[K, List[R]] = {}
        for item in right:
            if self.right_key(item) not in self.right_dict:
                self.right_dict[self.right_key(item)] = [item]
            else:
                self.right_dict[self.right_key(item)].append(item)

    def __iter__(self):
        return self

    def __next__(self) -> tuple[L, List[R] | None]:
        left: L = next(self.left)
        right: List[R] | None = self.right_dict.get(self.left_key(left))
        return left, right


class Scan[T]:
    iterable: Iterator[T]
    current: T | None = None
    acc: T | None = None
    operation: Callable[[T, T], T]

    def __init__(self, iterable, operation: Callable[[T, T], T]):
        self.iterable = iter(iterable)
        self.operation = operation

    def __iter__(self):
        return self

    def __next__(self):
        self.current = next(self.iterable)
        if self.acc is None:
            self.acc = self.current
        else:
            self.acc = self.operation(self.acc, self.current)
        return self.acc


if __name__ == "__main__":
    for i in Scan[int]([1, 2, 3, 4, 5], lambda x, y: x + y):
        print(i)

    for i in Scan[str](["a", "b", "c", "d", "e"], lambda x, y: x + y):
        print(i)
