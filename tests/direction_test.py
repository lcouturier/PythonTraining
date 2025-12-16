import pytest

from exo1 import Direction, Rotation


class TestDirection:
    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("L", Direction.LEFT),
            ("R", Direction.RIGHT),
        ],
    )
    def test_from_string_valid(self, input_str, expected):
        assert Direction.from_string(input_str) == expected

    @pytest.mark.parametrize(
        "invalid_str", ["", "X", "LEFT", "RIGHT", "l", "r", None, 5]
    )
    def test_from_string_invalid(self, invalid_str):
        with pytest.raises((ValueError, TypeError)):
            Direction.from_string(invalid_str)

    def test_direction_enum_members(self):
        assert Direction.LEFT.value == "L"
        assert Direction.RIGHT.value == "R"
        assert Direction.INVALID.value == "INVALID"


class TestRotation:
    def test_from_string_valid_left(self):
        rot = Rotation.from_string("L10")
        assert rot.direction == Direction.LEFT
        assert rot.value == 10

    def test_from_string_valid_right(self):
        rot = Rotation.from_string("R99")
        assert rot.direction == Direction.RIGHT
        assert rot.value == 99

    @pytest.mark.parametrize(
        "bad_input", ["X10", "L", "R", "", "L-5", "Labc", "10L", None, "L"]
    )
    def test_from_string_invalid(self, bad_input):
        with pytest.raises(Exception):
            Rotation.from_string(bad_input)

    def test_rotation_repr(self):
        rot = Rotation(Direction.LEFT, 25)
        assert repr(rot) == f"Rotation(direction={Direction.LEFT!r}, value=25)"
