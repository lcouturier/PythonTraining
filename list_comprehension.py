from datetime import datetime, timedelta
import itertools as it
from utils import unfold


def main():
    people = ["John", "Paul", "George", "Ringo", "George", "Paul"]

    result: list[str] = [person.upper() for person in people if person != "George"]
    print(result)


def inc(x: datetime) -> datetime:
    return x + timedelta(days=5)


def use_generator() -> None:
    generator = unfold(datetime.now(), inc)
    items = list(it.takewhile(lambda x: x.day < 31, generator))
    print(items)


if __name__ == "__main__":
    use_generator()
