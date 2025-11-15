from dataclasses import dataclass
from typing import Generic, TypeVar, Callable, cast

T = TypeVar("T")
U = TypeVar("U")


@dataclass(frozen=True)
class Result(Generic[T]):
    def is_success(self) -> bool:
        return isinstance(self, Success)

    def is_failure(self) -> bool:
        return isinstance(self, Failure)

    @staticmethod
    def of(data: T) -> "Result[T]":
        return Success(data=data)

    @staticmethod
    def failure(error_message: str) -> "Result[T]":
        return Failure(error=Exception(error_message))

    @staticmethod
    def from_exception(error: Exception) -> "Result[T]":
        return Failure(error=error)

    def map(self, fn: Callable[[T], U]) -> "Result[U]":
        if isinstance(self, Success):
            return Success(fn(self.data))
        return cast(Result[U], self)

    def and_then(self, fn: Callable[[T], "Result[U]"]) -> "Result[U]":
        if isinstance(self, Success):
            try:
                return fn(self.data)
            except Exception as e:
                return Failure(e)
        return cast(Result[U], self)

    def unwrap(self) -> T:
        if isinstance(self, Success):
            return self.data

        assert isinstance(self, Failure)
        raise self.error

    def unwrap_or(self, default: Callable[[], T]) -> T:
        if isinstance(self, Success):
            return self.data
        return default()


@dataclass(frozen=True)
class Success(Result[T]):
    data: T


@dataclass(frozen=True)
class Failure(Result[T]):
    error: Exception


def parse_int(s: str) -> Result[int]:
    try:
        return Success(int(s))
    except Exception as e:
        return Failure(e)


def reciprocal(x: int) -> Result[float]:
    if x == 0:
        return Failure(ZeroDivisionError("division by zero"))
    return Success(1 / x)


if __name__ == "__main__":
    res = parse_int("10").and_then(reciprocal).map(lambda x: x * 2)
    print(res.unwrap())
