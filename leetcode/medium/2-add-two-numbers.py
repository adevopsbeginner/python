"""
2. Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
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
    def leetcode(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int1 = 0
        factor = 1
        while l1:
            node = l1
            int1 = int1+node.val*factor
            factor *= 10
            l1 = l1.next
        int2 = 0
        factor = 1
        while l2:
            node = l2
            int2 = int2+node.val*factor
            factor *= 10
            l2 = l2.next
        int12 = int1+int2
        #print(int1,int2,int12)
        result = None
        index = None
        while int12 >= 0:
            node_val = int12%10
            #print(111,node_val, int12)
            node = ListNode(node_val)
            if result == None:
                result = node
                index = result
            else:
                index.next = node
                index = node

            int12 //= 10
            #print(222,node_val, int12)
            if int12 == 0:
                break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
