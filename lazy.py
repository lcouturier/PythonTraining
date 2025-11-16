from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")


class Lazy(Generic[T]):
    data: T
    is_evaluted: bool = False

    def __init__(self, f: Callable):
        self.f = f

    def __call__(self):
        if not self.is_evaluted:
            self.data = self.f()
            self.is_evaluted = True
        return self.data

    def __repr__(self):
        return f"Lazy({self.f})"

    def __str__(self):
        return f"Lazy({self.f}) has value: {self.is_evaluted}"

    def __bool__(self):
        return self.is_evaluted

    @staticmethod
    def of(value: Callable) -> "Lazy":
        return Lazy(lambda: value)

    @property
    def has_value(self) -> bool:
        """
        Check if the lazy value has been evaluated.

        :return: True if the value has been evaluated, False otherwise.
        :rtype: bool
        """
        return self.is_evaluted

    @property
    def is_empty(self) -> bool:
        """
        Check if the lazy value is empty.

        :return: True if the value is empty, False otherwise.
        :rtype: bool
        """
        return not self.is_evaluted

    @property
    def value(self):
        if not self.is_evaluted:
            self.data = self.f()
            self.is_evaluted = True
        return self.data

    def reset(self):
        self.is_evaluted = False


def my_function():
    return "Hello, World!"


if __name__ == "__main__":
    lazy = Lazy[List[int]](lambda: [1, 2, 3])
    print(lazy())
    print(lazy())

    print("----")
    lazy = Lazy[str](my_function)
    print(str(lazy))
    print(lazy.has_value)
    print(lazy.value)
    print(lazy.has_value)
    print(str(lazy))
    lazy.reset()
    print(lazy.has_value)
    print(lazy.value)
    print(lazy.has_value)
    print(str(lazy))
