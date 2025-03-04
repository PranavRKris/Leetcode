# Problem: 209 Minimum Size Subarray Sum
# Difficulty: Medium
# left 0 and right will iterate the length of the array, and total is kept track of
# pointer r is incremented till the total is greater then target then we'll check the min of output, 
# # substract l value and increment l

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        out = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                out = min(r-l+1, out)
                total -= nums[l]
                l += 1
        return 0 if out == float("inf") else out