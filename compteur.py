from typing import Any


class Compteur:
    def __init__(self, value: int = 0) -> None:
        self._value: int = value

    @property
    def value(self) -> int:
        return self._value

    def __iadd__(self, other: Any) -> "Compteur":
        if not isinstance(other, int):
            raise TypeError(f"Operand must be int, not {type(other).__name__}")
        self._value += other
        return self

    def __isub__(self, other: Any) -> "Compteur":
        if not isinstance(other, int):
            raise TypeError(f"Operand must be int, not {type(other).__name__}")
        self._value -= other
        return self

    def __repr__(self) -> str:
        return f"Compteur({self._value})"

    def __str__(self) -> str:
        return str(self._value)

    def reset(self) -> None:
        self._value = 0
