def first_occurence_index(haystack, needle):
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i: i + m] == needle:
            return i
    return -1


if __name__ == '__main__':
    print(first_occurence_index('hello', 'll'))
