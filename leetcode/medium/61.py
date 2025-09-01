"""
61. Rotate List
Solved
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ll = 0
        current = head
        while current:
            current = current.next
            ll += 1
            
        if ll <= 1:
            return head
        k %= ll
        if k == 0:
            return head
        current = head
        for ii in range(ll-k):
            p = current
            current = p.next
        p.next = None
        newhead = current
        while current:
            p = current
            current = p.next
        p.next = head
        head = newhead
        return head


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
