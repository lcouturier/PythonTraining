from dataclasses import dataclass
from enum import Enum
from typing import Iterator


items = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    INVALID = "INVALID"

    @classmethod
    def from_string(cls, value: str) -> "Direction":
        match value:
            case "L":
                return cls.LEFT
            case "R":
                return cls.RIGHT
            case _:
                return cls.INVALID


@dataclass
class Rotation:
    direction: Direction
    value: int


def read_file(filename: str) -> Iterator[str]:
    with open(filename, "r") as file:
        yield from (line.strip("\n") for line in file)


def translate_to_rotation(item: str) -> Rotation:
    direction = item[0]
    value = item[1:]
    return Rotation(Direction.from_string(direction), int(value))


def filter_direction(items):
    return filter(lambda x: x[0] in ["L", "R"], items)


def get_rotations(items: list[str]) -> Iterator[Rotation]:
    return map(translate_to_rotation, filter(filter_direction, items))


def process_rotations(items) -> int:
    count = 0
    start = 50
    MAX_VALUE = 100

    for item in get_rotations(items):
        match item.direction:
            case Direction.LEFT:
                temp = (start - item.value) % MAX_VALUE
                start = temp if (temp >= 0) else MAX_VALUE + temp
            case Direction.RIGHT:
                temp = (start + item.value) % MAX_VALUE
                start = temp - MAX_VALUE if (temp >= MAX_VALUE) else temp
            case Direction.INVALID:
                raise ValueError("Invalid direction in item: {}".format(item))

        if start == 0:
            count += 1

    return count


if __name__ == "__main__":
    items = read_file("exo1.txt")
    count = process_rotations(items)
    print(count)
