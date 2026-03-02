from typing import Callable, Iterable, Iterator


def accumulate[T](iterable: Iterable[T], operation: Callable[[T, T], T]) -> Iterator[T]:
    acc: T | None = None
    for item in iterable:
        if acc is None:
            acc = item
        else:
            acc = operation(acc, item)
        yield acc


def separated_by[T](iterable: Iterable[T], separator: T) -> Iterator[T]:
    first = True
    for item in iterable:
        if not first:
            yield separator
        yield item
        first = False


def pairwise[T](iterable: Iterable[T]) -> Iterator[tuple[T, T]]:
    iterator = iter(iterable)

    first = True
    for item in iterator:
        if first:
            previous = item
            first = False
        else:
            yield (previous, item)
            previous = item


def chunked[T](iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    iterator = iter(iterable)
    while True:
        chunk = []
        for _ in range(size):
            try:
                chunk.append(next(iterator))
            except StopIteration:
                if chunk:
                    yield chunk
                return
        yield chunk


def cycle[T](iterable: Iterable[T]) -> Iterator[T]:
    while True:
        for item in iterable:
            yield item


def group_by[T, E](
    iterable: Iterable[T],
    key: Callable[[T], T],
    transform=lambda x: x,
):
    """
    Groups the elements of the iterable by the key.

    Args:
        iterable: The iterable to group.
        key: The key to group by.
        transform: The transform to apply to the grouped elements.

    Returns:
        An iterator of tuples (key, transformed_group).

    Example:
        >>> list(group_by([1, 2, 3, 3, 3, 4, 5], lambda x: x % 2 == 0, len))
        [(False, 5), (True, 2)]
    """
    values: dict[T, list[T]] = {}

    for item in iterable:
        if key(item) not in values:
            values[key(item)] = [item]
        else:
            values[key(item)].append(item)

    for k, v in values.items():
        yield k, transform(v)


def count_by[T](
    iterable: Iterable[T], key: Callable[[T], T] = lambda x: x
) -> dict[T, int]:
    values: dict[T, int] = {}
    for item in iterable:
        if item not in values:
            values[item] = 1
        else:
            values[item] += 1
    return values


def distinct_by[T](
    iterable: Iterable[T], key: Callable[[T], T] = lambda x: x
) -> Iterator[T]:
    seen = set()
    for item in iterable:
        if key(item) not in seen:
            seen.add(key(item))
            yield item


def windowed[T](iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    items = list(iterable)
    for i in range(len(items) - size + 1):
        yield items[i : i + size]


if __name__ == "__main__":
    accumulate_result: Iterator[int] = accumulate([1, 2, 3, 4, 5], lambda x, y: x + y)
    print(list(accumulate_result))

    separated_result: Iterator[int] = separated_by([1, 2, 3, 4, 5], 0)
    print(list(separated_result))

    pairwise_result: Iterator[tuple[int, int]] = pairwise([1, 2, 3, 4, 5])
    print(list(pairwise_result))

    chunked_result: Iterator[list[int]] = chunked([1, 2, 3, 4, 5], 2)
    print(list(chunked_result))

    group_by_result: dict[int, list[int]] = group_by(
        [1, 2, 3, 3, 3, 4, 5], lambda x: x % 2 == 0
    )
    print(group_by_result)

    count_by_result: dict[int, int] = count_by([1, 2, 3, 3, 3, 4, 4, 5])
    print(count_by_result)

    distinct_by_result: Iterator[int] = distinct_by([1, 2, 3, 3, 3, 4, 4, 5])
    print(list(distinct_by_result))

    windowed_result: Iterator[list[int]] = windowed([1, 2, 3, 4, 5], 3)
    print(list(windowed_result))
