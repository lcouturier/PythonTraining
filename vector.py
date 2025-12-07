from typing import Any


class Vector:
    __slots__ = ("_x", "_y")

    def __init__(self, x: int = 0, y: int = 0) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("x and y must be integers")
        if x < 0 or y < 0:
            raise ValueError("x and y cannot be negative")
        object.__setattr__(self, "_x", x)
        object.__setattr__(self, "_y", y)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x cannot be negative")
        object.__setattr__(self, "_x", value)

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y cannot be negative")
        object.__setattr__(self, "_y", value)

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    def __repr__(self) -> str:
        return f"Vector({self._x}, {self._y})"

    def __add__(self, other: Any) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other: Any) -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, scalar: Any) -> "Vector":
        if not isinstance(scalar, int):
            return NotImplemented
        return Vector(self._x * scalar, self._y * scalar)

    def dot(self, other: Any) -> int:
        if not isinstance(other, Vector):
            raise TypeError("dot product only supported with another Vector")
        return self._x * other._x + self._y * other._y

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Vector):
            return False
        return self._x == other._x and self._y == other._y

    def __ne__(self, other: Any) -> bool:
        return not self == other


def main():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("v1:", v1)
    print("v2:", v2)

    print(str(v1))
    print(str(v2))

    print(v1 == v2)
    print(v1 != v2)

    print("Addition:", v1 + v2)
    print("Subtraction:", v1 - v2)
    print("Scalar Multiplication:", v1 * 2)
    print("Dot Product:", v1.dot(v2))


if __name__ == "__main__":
    main()
