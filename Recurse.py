def tail(items):
    return items[1:]


def head(items):
    return items[0]


def max_items(items):
    if not items:
        return 0
    max_item = items[0]
    for item in items[1:]:
        max_item = max(max_item, item)
    return max_item


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
