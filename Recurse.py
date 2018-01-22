def tail(items):
    return items[1:]


def head(items):
    return items[0]


def max(items):
    if len(items) == 0:
        return 0
    else:
        result = sum(tail(items))
        if head(items) > result:
            return head(items)
        else:
            return result


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
