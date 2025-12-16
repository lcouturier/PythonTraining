from dataclasses import dataclass
from enum import Enum
from functools import reduce
from typing import Callable, Iterator
from typing_extensions import Iterable

import requests as request
import browser_cookie3

from annotations import my_lru_cache
from utils import measure


class Source(Enum):
    FILE = "file"
    URL = "url"


type Loader = Callable[[str], Iterator[str]]


def load_from_file(filename: str) -> Iterator[str]:
    with open(filename, "r") as file:
        yield from (line.strip("\n") for line in file)


def load_from_web(url: str) -> Iterator[str]:
    session_cookie = get_session_cookie(domain_name="adventofcode.com")
    cookies = {"session": session_cookie}
    headers = {"User-Agent": "python-requests"}
    with request.get(url, cookies=cookies, headers=headers) as response:
        if response.status_code != 200:
            raise ValueError(f"Invalid response code: {response.status_code}")
        yield from (line.strip() for line in response.text.split("\n") if line.strip())


def load_from_source(*, source: Source, source_name: str) -> Iterator[str]:
    loaders: dict[Source, Loader] = {
        Source.FILE: load_from_file,
        Source.URL: load_from_web,
    }
    loader = loaders.get(source)
    if loader is None:
        raise ValueError(f"Unknown source: {source}")
    return loader(source_name)


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"
    INVALID = "INVALID"

    @classmethod
    def from_string(cls, value: str) -> "Direction":
        if value not in ["L", "R"]:
            raise ValueError(f"Invalid direction: {value}")
        return cls.LEFT if value == "L" else cls.RIGHT


@dataclass
class Rotation:
    direction: Direction
    value: int

    @staticmethod
    def from_string(item: str) -> "Rotation":
        direction = Direction.from_string(item[0])
        if (item[1:] == "") or (not item[1:].isnumeric()):
            raise ValueError(f"Invalid rotation: {item}")
        value = int(item[1:])
        return Rotation(direction, value)


@my_lru_cache(10)
def get_session_cookie(*, domain_name: str) -> str:
    cookies = browser_cookie3.chrome(domain_name=domain_name)
    session = next(
        (cookie.value for cookie in cookies if cookie.name == "session"), None
    )

    if session is not None:
        return session
    raise ValueError(
        f"Cookie 'session' introuvable. Es-tu connecté au domaine {domain_name} ?"
    )


# def acc_func(acc: tuple[int, int], item: Rotation) -> tuple[int, int]:
#     MAX_VALUE = 100
#     apply = {
#         Direction.LEFT: lambda x, y: (x - y) % MAX_VALUE,
#         Direction.RIGHT: lambda x, y: (x + y) % MAX_VALUE,
#     }

#     start_val, count = acc
#     new_start = apply[item.direction](start_val, item.value)
#     count += new_start == 0
#     return (new_start, count)

type AccFunc = Callable[[tuple[int, int], Rotation], tuple[int, int]]


def acc_func_core() -> AccFunc:
    MAX_VALUE = 100
    apply = {
        Direction.LEFT: lambda x, y: (x - y) % MAX_VALUE,
        Direction.RIGHT: lambda x, y: (x + y) % MAX_VALUE,
    }

    def inner(acc: tuple[int, int], item: Rotation) -> tuple[int, int]:
        start_val, count = acc
        new_start = apply[item.direction](start_val, item.value)
        count += new_start == 0
        return (new_start, count)

    return inner


def process_rotations(
    start: int,
    items: Iterable[str],
    acc: AccFunc,
) -> int:
    rotations: Iterator[Rotation] = (
        Rotation.from_string(item) for item in items if item[0] in ["L", "R"]
    )

    _, count = reduce(acc, rotations, (start, 0))
    return count


@measure
def main():
    items = load_from_source(
        source=Source.URL, source_name="https://adventofcode.com/2025/day/1/input"
    )
    count = process_rotations(50, items, acc_func_core())
    print(count)


if __name__ == "__main__":
    main()
