# Definition for singly-linked list.
# Get Length, k%length and check if k is 0. Create a dummy and traverse till length-k-1.
# Set newHead to curr.next, curr.next to None, tail.next to head and return newHead

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head

        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head
        return newHead