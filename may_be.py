from typing import Generic, TypeVar, Callable

R = TypeVar("R")  # Value type


class Either(Generic[R]):
    def is_left(self) -> bool:
        return isinstance(self, Left)

    def is_right(self) -> bool:
        return isinstance(self, Right)

    def map(self, f: Callable[[R], R]) -> "Either[R]":
        if self.is_right():
            return Right(f(self.value))
        return self

    def map_left(self, f: Callable[[Exception], Exception]) -> "Either[R]":
        if self.is_left():
            return Left(f(self.error))
        return self


class Left(Either[R]):
    __slots__ = ("_error",)

    def __init__(self, error: Exception) -> None:
        self._error = error

    @property
    def error(self) -> Exception:
        return self._error

    @property
    def value(self) -> None:
        return None

    def __repr__(self) -> str:
        return f"Left({self._error!r})"


class Right(Either[R]):
    __slots__ = ("_value",)

    def __init__(self, value: R) -> None:
        self._value = value

    @property
    def value(self) -> R:
        return self._value

    @property
    def error(self) -> None:
        return None

    def __repr__(self) -> str:
        return f"Right({self._value!r})"
