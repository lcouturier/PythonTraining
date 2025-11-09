class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be an instance of Vector")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be an instance of Vector")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be a number")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            if scalar != 0:
                return Vector(self.x / scalar, self.y / scalar)
            raise ValueError("Cannot divide by zero")
        raise TypeError("Operand must be a number")

    def dot(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Operand must be an instance of Vector")

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


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
    print("Scalar Division:", v1 / 2)
    print("Dot Product:", v1.dot(v2))


if __name__ == '__main__':
    main()
