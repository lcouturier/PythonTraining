from dataclasses import dataclass
from enum import Enum
from functools import reduce
from typing import Iterator
from annotations import composable


# items = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    INVALID = "INVALID"

    @classmethod
    def from_string(cls, value: str) -> "Direction":
        if value not in ["L", "R"]:
            return ValueError(f"Invalid direction: {value}")
        return cls.LEFT if value == "L" else cls.RIGHT


@dataclass
class Rotation:
    direction: Direction
    value: int


@composable
def read_file(filename: str) -> Iterator[str]:
    with open(filename, "r") as file:
        yield from (line.strip("\n") for line in file)


def translate_to_rotation(item: str) -> Rotation:
    direction = item[0]
    value = item[1:]
    return Rotation(Direction.from_string(direction), int(value))


def acc_func(acc, item: Rotation):
    MAX_VALUE = 100
    apply = {
        Direction.LEFT: lambda x, y: (x - y) % MAX_VALUE,
        Direction.RIGHT: lambda x, y: (x + y) % MAX_VALUE,
    }

    start_val, count = acc
    new_start = apply[item.direction](start_val, item.value)
    count += new_start == 0
    return (new_start, count)


def process_rotations(start: int, items: list[str]) -> int:
    items = (translate_to_rotation(item) for item in items if item[0] in ["L", "R"])
    _, count = reduce(acc_func, items, (start, 0))
    return count


if __name__ == "__main__":
    count = process_rotations(50, read_file("exo1.txt"))
    print(count)
