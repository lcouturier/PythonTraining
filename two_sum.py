def two_sum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum2(nums: list[int], target: int) -> list[int]:
    num_map: dict[int, int] = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement: int = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []


def two_sum3(nums: list[int], target: int) -> list[int]:
    """
    Returns a list of indices of two elements in the given list that
    add up to the given target.

    :param nums: A list of integers.
    :type nums: list[int]
    :param target: The target sum.
    :type target: int
    :return: A list of indices of two elements in the given list that
        add up to the given target.
    :rtype: list[int]
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


if __name__ == "__main__":
    r = two_sum3([2, 7, 11, 15], 9)
    print(r)
