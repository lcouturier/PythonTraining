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


class Chunked[T]:
    def __init__(self, iterable, size: int):
        self.iterable = iter(iterable)
        self.size = size

    def __iter__(self):
        return self

    def __next__(self) -> list[T]:
        chunk: list[T] = []

        for _ in range(self.size):
            try:
                chunk.append(next(self.iterable))
            except StopIteration:
                if chunk:
                    return chunk
                raise

        return chunk


class PairWise[T]:
    first: bool = True

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.prev = next(self.iterable)

    def __iter__(self):
        return self

    def __next__(self) -> tuple[T, T]:
        if self.first:
            self.first = False
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


class InnerJoin[L, R, K]:
    left_key: Callable[[L], K]
    right_key: Callable[[R], K]

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
        if right is None:
            raise StopIteration
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


class UnFold[T]:
    """
    Unfold is the opposite of fold. It takes a seed value and a function that generates the next value.

    Example:
    >>> for i in UnFold(1, lambda x: x * 2):
    ...     print(i)
    ...     if i > 10:
    ...         break
    1
    2
    4
    8
    16
    """

    def __init__(self, start: T, operation: Callable[[T], T]):
        self.start = start
        self.operation = operation

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        self.start = self.operation(self.start)
        return result


if __name__ == "__main__":
    pass
