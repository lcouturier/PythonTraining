from functools import partial

import utils


def two_sum1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum2(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        num_map[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]
    return []


def two_sum3(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


if __name__ == '__main__':
    c1 = partial(two_sum1, [2, 7, 11, 15])
    s1 = utils.measure(c1)
    c2 = partial(two_sum2, [2, 7, 11, 15])
    s2 = utils.measure(c2)
    c3 = partial(two_sum3, [2, 7, 11, 15])
    s3 = utils.measure(c3)

    print(s1(9))
    print(s2(9))
    print(s3(9))
