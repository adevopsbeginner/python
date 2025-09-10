"""
92. Reverse Linked List II
Medium
Topics
￼
Companies
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:

￼
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
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
    def leetcode(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        current = head
        if left == 1:
            reversed_head = head
            reversed_tail = head
            current = reversed_head.next
            reversed_head.next = None
            head = None
        else:
            for ii in range(left-2):
                current = current.next

            tail = current
            current = current.next
            reversed_head = current
            current = current.next
            reversed_head.next = None
            reversed_tail = reversed_head
            #print(reversed_head.val, reversed_tail.val)
        
        for ii in range(right-left-1):
            reversed_head, current.next, current = current, reversed_head, current.next

        reversed_tail.next = current.next
        current.next = reversed_head
        reversed_head = current

        if head == None:
            head = reversed_head
        else:
            tail.next = reversed_head

        return head


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
