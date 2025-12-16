import random


def left_join(left, right, key_left, key_right, resultSelector):
    index = {}
    for r in right:
        k = key_right(r)
        index[k] = index.get(k, []) + [r]

    for l in left:  # noqa: E741
        key = key_left(l)
        if key not in index:
            yield resultSelector(l, None)
        else:
            for r in index[key]:
                yield resultSelector(l, r)


def join(*, left, right, key_left, key_right, resultSelector=lambda x, y: (x, y)):
    index = {}
    for r in right:
        k = key_right(r)
        index[k] = index.get(k, []) + [r]
    for l in left:  # noqa: E741
        key = key_left(l)
        if key in index:
            for r in index[key]:
                yield resultSelector(l, r)


if __name__ == "__main__":
    left = [random.randint(1, 10) for _ in range(10)]
    right = [random.randint(1, 10) for _ in range(10)]
    print(
        list(
            filter(
                lambda x: x[1] is not None,
                join(
                    left=left,
                    right=right,
                    key_left=lambda x: x,
                    key_right=lambda x: x,
                ),
            )
        )
    )
