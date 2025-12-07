import pytest
from vector import Vector


def test_vector_initialization():
    v = Vector(5, 7)
    assert v.x == 5
    assert v.y == 7


def test_vector_default_initialization():
    v = Vector()
    assert v.x == 0
    assert v.y == 0


def test_vector_invalid_type_initialization():
    with pytest.raises(TypeError):
        Vector(1.2, 3)
    with pytest.raises(TypeError):
        Vector(3, "4")


def test_vector_negative_initialization():
    with pytest.raises(ValueError):
        Vector(-1, 2)
    with pytest.raises(ValueError):
        Vector(2, -3)


def test_vector_str_and_repr():
    v = Vector(2, 8)
    assert str(v) == "(2, 8)"
    assert repr(v) == "Vector(2, 8)"


def test_vector_equality():
    v1 = Vector(1, 1)
    v2 = Vector(1, 1)
    v3 = Vector(2, 3)
    assert v1 == v2
    assert v1 != v3


def test_vector_addition():
    v1 = Vector(2, 3)
    v2 = Vector(1, 4)
    v3 = v1 + v2
    assert isinstance(v3, Vector)
    assert v3.x == 3 and v3.y == 7


def test_vector_addition_invalid_type():
    v1 = Vector(1, 1)
    assert (v1 + "abc") == NotImplemented or type(v1 + "abc") is type(
        NotImplemented
    )  # Defensive


def test_vector_subtraction():
    v1 = Vector(5, 7)
    v2 = Vector(2, 3)
    v3 = v1 - v2
    assert v3 == Vector(3, 4)


def test_vector_subtraction_invalid_type():
    v1 = Vector(1, 1)
    assert (v1 - 12.0) == NotImplemented or type(v1 - 12.0) is type(NotImplemented)


def test_vector_scalar_multiplication():
    v1 = Vector(2, 3)
    v2 = v1 * 4
    assert v2.x == 8 and v2.y == 12


def test_vector_scalar_multiplication_invalid_type():
    v1 = Vector(2, 2)
    result = v1 * "abc"
    assert result == NotImplemented or type(result) is type(NotImplemented)


def test_vector_dot_product():
    v1 = Vector(2, 5)
    v2 = Vector(3, 4)
    assert v1.dot(v2) == 2 * 3 + 5 * 4


def test_vector_dot_product_invalid_type():
    v1 = Vector(1, 2)
    with pytest.raises(TypeError):
        v1.dot((3, 4))


def test_vector_x_setter_valid():
    v = Vector(3, 4)
    v.x = 10
    assert v.x == 10


def test_vector_y_setter_valid():
    v = Vector(3, 4)
    v.y = 7
    assert v.y == 7


def test_vector_x_setter_invalid_type():
    v = Vector(2, 2)
    with pytest.raises(TypeError):
        v.x = "bad"


def test_vector_x_setter_negative():
    v = Vector(2, 2)
    with pytest.raises(ValueError):
        v.x = -10


def test_vector_y_setter_invalid_type():
    v = Vector(2, 2)
    with pytest.raises(TypeError):
        v.y = 3.5


def test_vector_y_setter_negative():
    v = Vector(2, 2)
    with pytest.raises(ValueError):
        v.y = -3
