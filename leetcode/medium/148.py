"""
148. Sort List
Solved
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
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
    def leetcode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ### 20250904
        if head == None:
            return head

        q = [[head.val, 0, head]]

        ### while with same val, heapq does not compare ListNode
        count = 1
        
        heapq.heapify(q)
        index = head.next
        while index:
            heapq.heappush(q, [index.val, count, index])
            index = index.next
            count += 1

        ll = len(q)
        _, _, result = heapq.heappop(q)
        index = result
        result.next = None
        for ii in range(ll-1):
            _, _, index.next = heappop(q)
            index = index.next
            index.next = None

        return result

        ### time limit exceeded
        if head == None:
            return head
        p = head
        c = p.next
        while c:
            #print(p.val,c.val)
            if c.val >= p.val:
                p = c
                c = p.next
                continue
            p.next = c.next
            c.next = None
            if c.val <= head.val:
                c.next = head
                head = c
                c = p.next
                continue
            ip = head
            ic = ip.next
            while c.val > ic.val:
                ip = ic
                ic = ic.next
            ip.next = c
            c.next = ic
            c = p.next
        return head


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
