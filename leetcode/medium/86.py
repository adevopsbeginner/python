"""
86. Partition List
Medium
Topics
premium lock icon
Companies
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
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
    def leetcode(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = None
        less_tail = None
        greater_head = None
        greater_tail = None

        while head:
            #print(head.val, less_head, greater_head)
            if head.val < x:
                if less_head == None:
                    less_head = head
                    less_tail = less_head
                else:
                    less_tail.next = head
                    less_tail = less_tail.next
            else:
                if greater_head == None:
                    greater_head = head
                    greater_tail = greater_head
                else:
                    greater_tail.next = head
                    greater_tail = greater_tail.next

            head = head.next
            
            if less_tail:
                less_tail.next = None
            if greater_tail:
                greater_tail.next = None

        if less_head == None:
            return greater_head
        
        if greater_head:
            less_tail.next = greater_head
        
        return less_head


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
