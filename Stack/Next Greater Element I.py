# 496. Next Greater Element I
# Difficulty: Easy
# Create hashmap of value and index of the first array
# 

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = index[val]
                res[idx] = curr
            if curr in index:
                stack.append(curr)
        return res
    
#nums1 = [4,1,2], nums2 = [1,3,4,2]
# i = 0, curr = 1, while loop doesnt satisfy, stack = [1]
# i = 1, curr = 3, stack is true and 3 > 1, val = 1, idx = 1, res = [-1, 3, -1], stack = [] as 3 not in index
# i = 2, curr = 4, while loop doesnt satisfy, stack = [4]
# i = 3, curr = 2, while loop doesnt satisfy as 2 < 4
# return res = [-1, 3, -1]
