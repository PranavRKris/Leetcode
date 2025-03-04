# Problem: 2. Add Two Numbers
# Difficulty: Medium
# check if l1 or l2 or carry is not null, get the val of l1 and l2, add them and carry
# set carry to val//10 and val to val%10

from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        test = ListNode()
        cur = test
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry

            carry = val //10
            val = val%10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return test.next