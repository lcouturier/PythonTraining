from typing import Callable


class Lazy:
    data = None

    def __init__(self, f: Callable):
        self.f = f

    def __call__(self):
        if self.data is None:
            self.data = self.f()
        return self.data

    def __repr__(self) -> str:
        return f"Lazy({self.f})"

    def __str__(self) -> str:
        return f"Lazy({self.f})"

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
        return self.data is not None

    @property
    def is_empty(self) -> bool:
        """
        Check if the lazy value is empty.

        :return: True if the value is empty, False otherwise.
        :rtype: bool
        """
        return self.data is None

    @property
    def value(self):
        return self()


def my_function():
    return "Hello, World!"


if __name__ == "__main__":
    lazy = Lazy(lambda: [1, 2, 3])
    print(lazy())
    print(lazy())

    print("----")
    lazy = Lazy(my_function)
    print(lazy.has_value)
    print(lazy.value)
    print(lazy.has_value)
