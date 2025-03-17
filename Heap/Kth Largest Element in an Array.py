# Medium
# For finding the largest element, we can use a min heap of size k.
# The heap keeps track of the k largest elements seen so far and after iterating throught he whole array
# the top element of the heap will be the kth largest element.


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for i in nums[k:]:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        
        return heap[0]
        