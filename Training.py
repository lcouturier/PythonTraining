# Exercises


import heapq
from utils import measure


def first_occurring_char(value):
    dic = {}
    for c in value:
        if c in dic:
            return c
        dic[c] = 1


@measure
def max_occurring_char(value: str) -> str:
    """
    Returns the character with the highest number of consecutive occurrences.
    If there are multiple, returns the first such character found.
    """
    if not value:
        raise ValueError("Input string must not be empty.")

    max_char = value[0]
    max_count = 1
    curr_char = value[0]
    curr_count = 1

    for c in value[1:]:
        if c == curr_char:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_char = curr_char
                max_count = curr_count
            curr_char = c
            curr_count = 1
    if curr_count > max_count:
        max_char = curr_char

    return max_char


@measure
def max_occurring_char_v1(value):
    frequency = {}
    for i in value:
        frequency[i] = frequency.get(i, 0) + 1

    heap = []
    for item, freq in frequency.items():
        heapq.heappush(heap, (freq, item))
        if len(heap) > 1:
            heapq.heappop(heap)

    return heap[0]


def main():
    items = "AABBBDDADDDDCCCBBAAAAAABBBDDADDDDCCCBBAAAAABBBDDADDDDCCCBBAAAAABBBDDADDDDCCCBBAAA"
    print(max_occurring_char(items))
    print(max_occurring_char_v1(items))


if __name__ == "__main__":
    main()
