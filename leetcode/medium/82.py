"""
82. Remove Duplicates from Sorted List II
Solved
Medium
Topics
premium lock icon
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
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
        ans = ListNode(-101)
        ans.next = head
        tmp = ans
        lt = []
        flag = 0
        tmp1 = ans
        tmp2 = tmp1.next
        while tmp2:
            if tmp2.next and tmp2.val == tmp2.next.val:
                tmp2.next = tmp2.next.next
                flag = 1
            elif flag == 1:
                tmp1.next = tmp2.next
                tmp2 = tmp2.next
                flag = 0
            else:
                tmp1 = tmp2
                tmp2 = tmp1.next
                flag = 0

        return ans.next


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
