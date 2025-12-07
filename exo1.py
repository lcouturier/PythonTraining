from dataclasses import dataclass
from enum import Enum
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


def get_rotations(items: list[str]) -> Iterator[Rotation]:
    return (translate_to_rotation(item) for item in items if item[0] in ["L", "R"])


def process_rotations(start: int, items: list[str]) -> int:
    MAX_VALUE = 100
    apply = {
        Direction.LEFT: lambda x, y: (x - y) % MAX_VALUE,
        Direction.RIGHT: lambda x, y: (x + y) % MAX_VALUE,
    }
    count = 0
    for item in get_rotations(items):
        start = apply[item.direction](start, item.value)
        count += start == 0
    return count


@composable
def compute_rotations(items):
    return process_rotations(50, items)


def pipeline(value, *funcs):
    for fn in funcs:
        value = fn(value)
    return value


if __name__ == "__main__":
    f = read_file >> compute_rotations

    print(f("exo1.txt"))
