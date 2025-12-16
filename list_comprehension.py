from datetime import datetime, timedelta
from utils import unfold


def main():
    people = ["John", "Paul", "George", "Ringo", "George", "Paul"]

    result: list[str] = [person.upper() for person in people if person != "George"]
    print(result)


def inc(x: datetime) -> datetime:
    return x + timedelta(days=1)


def use_generator() -> None:
    generator = unfold(datetime.now(), inc)

    print(next(generator))
    print(next(generator))
    print(next(generator))


if __name__ == "__main__":
    use_generator()
