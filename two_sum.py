from utils import measure


@measure
def two_sum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


@measure
def two_sum2(nums: list[int], target: int) -> list[int]:
    num_map: dict[int, int] = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement: int = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []


@measure
def two_sum3(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


if __name__ == "__main__":
    items = [2, 7, 11, 15, 9, 12, 5, 4]
    print(two_sum1(items, 16))
    print(two_sum2(items, 16))
    print(two_sum3(items, 16))
