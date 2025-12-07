from typing import Callable, Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")


class Result(Generic[T, E]):
    __slots__ = ()

    def is_success(self) -> bool:
        return isinstance(self, Success)

    def is_failure(self) -> bool:
        return isinstance(self, Failure)

    @staticmethod
    def of(value: T = None, error: E = None) -> "Result[T, E]":
        if error is not None:
            return Failure(error)
        return Success(value)

    def when(self, on_success: Callable[[T], None], on_failure: Callable[[E], None]):
        if self.is_success():
            on_success(self.value)
        else:
            on_failure(self.error)

    def map(self, f: Callable[[T], E]) -> "Result[T, E]":
        if self.is_success():
            return Success(f(self.value))
        else:
            return Failure(self.error)


class Success(Result[T, E]):
    __slots__ = ("_value",)

    def __init__(self, value: T):
        self._value = value

    @property
    def value(self) -> T:
        return self._value

    @property
    def error(self) -> None:
        return None

    def __repr__(self) -> str:
        return f"Success({self._value!r})"


class Failure(Result[T, E]):
    __slots__ = ("_error",)

    def __init__(self, error: E):
        self._error = error

    @property
    def value(self) -> None:
        return None

    @property
    def error(self) -> E:
        return self._error

    def __repr__(self) -> str:
        return f"Failure({self._error!r})"
