# 1920. Build Array from Permutation

Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.


A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

## Takeaways

Within this exercise, the run time was improved by re running the solution in
order. However this is cheating because you are taking advantage of caching.