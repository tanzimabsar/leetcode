import random
from typing import List, Tuple
from collections import deque

def remove_duplicates(nums: List[int]) -> tuple[int, list[int]]:
    """Given an array of integers return the amount of
    unique chars and de deuplicate the error

    A simple iterative solution mutates the array in place
    using pop and returns that along with its len
    """

    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return nums


def test_remove_duplicates():
    nums = sorted(random.sample(range(100*2), 10*2))
    assert remove_duplicates(nums) == sorted(list(set(nums)))
