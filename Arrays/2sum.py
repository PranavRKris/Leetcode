# Create a hashmap of the difference between target and each element. 
# If the difference is in the hashmap, return the indices of the element and the difference.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [dict[diff], i]
            dict[n] = i