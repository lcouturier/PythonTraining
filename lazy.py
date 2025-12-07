from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")


class Lazy(Generic[T]):
    """
    Lazily computes and caches the result of a function upon first access.
    """

    __slots__ = ("_func", "_evaluated", "_value")

    def __init__(self, f: Callable[[], T]) -> None:
        self._func: Callable[[], T] = f
        self._evaluated: bool = False
        self._value: T | None = None

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"Lazy({self._func!r})"

    def __str__(self) -> str:
        return f"value: {self.value!r}"

    def __bool__(self) -> bool:
        return self._evaluated

    @staticmethod
    def of(func: Callable[[], T]) -> "Lazy[T]":
        return Lazy(func)

    @property
    def has_value(self) -> bool:
        return self._evaluated

    @property
    def is_empty(self) -> bool:
        return not self._evaluated

    @property
    def value(self) -> T:
        if not self._evaluated:
            self._value = self._func()
            self._evaluated = True
        # Defensive for mypy: after _evaluated is True, _value is not None.
        assert self._value is not None
        return self._value

    def reset(self) -> None:
        self._evaluated = False
        self._value = None


def my_function():
    return "Hello, World!"


if __name__ == "__main__":
    lazy = Lazy[List[int]](lambda: [1, 2, 3])
    print(lazy())
    print(lazy())

    print("----")
    lazy_str = Lazy[str](my_function)
    print(str(lazy_str))
    print(lazy_str.has_value)
    print(lazy_str.value)
    print(lazy_str.has_value)
    print(str(lazy_str))
    lazy_str.reset()
    print("reset")
    print(lazy_str.has_value)
    print(lazy_str.value)
    print(lazy_str.has_value)
    print(str(lazy_str))
