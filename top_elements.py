import heapq
import random

from utils import measure


@measure
def top_k_elements2(nums, k):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:k]
    return [item[0] for item in items]


@measure
def top_k_elements(nums, k):
    frequency = {}
    for i in nums:
        frequency[i] = frequency.get(i, 0) + 1

    heap = []
    for num, freq in frequency.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


if __name__ == "__main__":
    nums = liste = [random.randint(1, 10) for _ in range(10000)]
    print(top_k_elements(nums, 2))
    print(top_k_elements2(nums, 2))
