from dataclasses import dataclass
from enum import Enum
from functools import reduce
from typing import Iterator
import requests as request
import browser_cookie3


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

    @staticmethod
    def from_string(item: str) -> "Rotation":
        direction = Direction.from_string(item[0])
        value = int(item[1:])
        return Rotation(direction, value)


def get_session_cookie(domain_name: str) -> str:
    cookies = browser_cookie3.chrome(domain_name=domain_name)
    session = next(
        (cookie.value for cookie in cookies if cookie.name == "session"), None
    )

    if session is not None:
        return session
    raise ValueError(
        f"Cookie 'session' introuvable. Es-tu connecté au domaine {domain_name} ?"
    )


def load_data_from_url(url: str, domain_name: str) -> Iterator[str]:
    session_cookie = get_session_cookie(domain_name)
    cookies = {"session": session_cookie}
    headers = {"User-Agent": "python-requests"}
    with request.get(url, cookies=cookies, headers=headers) as response:
        if response.status_code != 200:
            raise ValueError(f"Invalid response code: {response.status_code}")
        yield from (line.strip() for line in response.text.split("\n") if len(line) > 0)


def read_file(filename: str) -> Iterator[str]:
    with open(filename, "r") as file:
        yield from (line.strip("\n") for line in file)


def acc_func(acc: tuple[int, int], item: Rotation):
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
    items = (Rotation.from_string(item) for item in items if item[0] in ["L", "R"])
    _, count = reduce(acc_func, items, (start, 0))
    return count


if __name__ == "__main__":
    # count = process_rotations(50, read_file("exo1.txt"))
    count = process_rotations(
        50,
        load_data_from_url(
            "https://adventofcode.com/2025/day/1/input", "adventofcode.com"
        ),
    )
    print(count)
