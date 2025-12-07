from typing import Iterable, List


def load_even_number_from_csv_file(file_path: str) -> List[int]:
    """Load even integers from a CSV file, one integer per line.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[int]: List of even integers found in the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        lines = (line.strip() for line in file)
        even_numbers = [
            number for line in lines if line and (number := int(line)) % 2 == 0
        ]
    return even_numbers


def get_even_number_first_version(start: int, stop: int, step: int) -> list[int]:
    """Return a list of even integers in range(start, stop, step)."""
    return [i for i in range(start, stop, step) if i % 2 == 0]


def return_even(items: Iterable[int]) -> List[int]:
    """
    Returns a list containing only the even integers from the provided iterable.

    Args:
        items (Iterable[int]): An iterable of integers.

    Returns:
        List[int]: A list of even integers.
    """
    return [i for i in items if i % 2 == 0]


def even_generator(start: int = 0) -> int:
    """
    Yield an infinite sequence of even integers, starting from `start`.

    If `start` is odd, yields the next even number greater than or equal to `start`.

    Args:
        start (int, optional): The starting integer for the sequence. Defaults to 0.

    Yields:
        int: The next even integer in the infinite sequence.
    """
    value = start if start % 2 == 0 else start + 1
    while True:
        yield value
        value += 2


def odd_generator():
    value = 1
    while True:
        yield 1
        value += 2
