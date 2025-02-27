# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# -> k % len(array) helps to reduce the number of rotations needed if k is greater 
# than or equal to the length of the array
# Just swap the values of the array from 0 to k-1, then k to len(array)-1, and finally 0 to len(array)-1

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r, nums):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        
        k = k % len(nums)
        reverse(0, len(nums)-1, nums)

        reverse(0, k-1, nums)

        reverse(k, len(nums)-1, nums)