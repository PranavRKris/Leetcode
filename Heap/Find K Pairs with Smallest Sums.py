# Medium
# Since both the arrays are sorted, the first values of the array will always be the smallest.
# then we can add the next smallest value from the second array and so on.
# We can use a heap to keep track of the smallest sum of the pairs.

from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        out = []

        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        len1, len2 = len(nums1), len(nums2)

        while k != 0:
            val, i, j = heappop(heap)

            out.append([nums1[i], nums2[j]])

            if j+1 < len2:
                heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            
            if j == 0 and i + 1 < len1:
                heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            k -= 1
        return out