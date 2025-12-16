def range(start, end, step=1):
    if step == 0:
        raise ValueError("step cannot be zero")
    if start < end and step > 0:
        current = start
        while current <= end:
            yield current
            current += step
    elif start > end and step < 0:
        current = start
        while current >= end:
            yield current
            current += step
    elif start == end:
        yield start


if __name__ == "__main__":
    for i in range(1, 10):
        print(i)

    for i in range(10, 1):
        print(i)
