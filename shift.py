def right_shift1(items, n):
    size = len(items)
    n = n % size
    return items[-n:] + items[:-n]


def right_shift2(items, n):
    size = len(items)
    for j in range(size - 1, 0, -1):
        temp = items[j]
        items[j] = items[j - 1]
        items[j - 1] = temp
    return items


def main():
    print(right_shift1([1, 2, 3, 4, 5], 1))
    print(right_shift2([1, 2, 3, 4, 5], 1))


if __name__ == "__main__":
    main()
