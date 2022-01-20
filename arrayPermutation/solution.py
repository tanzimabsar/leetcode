"""
Given an array such as [1,2,3,4]
Iterate over the array such that a new array is returned
with each index position as the value of the new array
[index[i] of [1,2,3,4]
"""

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[item] for item in nums]


