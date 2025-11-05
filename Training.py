# Exercises


def first_occurring_char(value):
    dic = {}
    for c in value:
        if c in dic:
            return c
        dic[c] = 1


def max_occurring_char(value):
    dic = {}
    i = 0
    previous = value[0]
    for c in value:
        if c in dic:
            if c == previous:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1
        else:
            dic[c] = 1
        i = i + 1
        previous = value[i - 1]

    d = {v: k for k, v in dic.items()}
    return d[max(d)]


def main():
    result = max_occuring_char("AABBBDDADDDDD")


if __name__ == '__main__':
    main()
