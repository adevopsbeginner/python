"""
234. Palindrome Linked List
Solved
Easy
Topics
Companies
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return True
        if head.next == None:
            return True

        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        a = count // 2
        b = count % 2
        # print(count, a, b)

        current = head
        l1 = head
        for ii in range(a-1):
            current = current.next
        l2 = current.next
        current.next = None
        if b:
            l2 = l2.next
        newl2 = None
        while l2:
            current = l2
            l2 = l2.next
            current.next = newl2
            newl2 = current
        l2 = newl2
        while l1 or l2:
            if l1 == None:
                return False
            if l2 == None:
                return False
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True

if __name__ == "__main__":
    app = Solution()
    a = [0,1,2,4,5,7]
    print(app.leetcode(a))
