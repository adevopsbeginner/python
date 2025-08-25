"""
633. Sum of Square Numbers
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false


Constraints:

0 <= c <= 231 - 1
"""

import string
import heapq
import math
from typing import List
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = math.isqrt(c - a * a)
            if a * a + b * b == c:
                return True
            a += 1

        return False

        a = 1
        a2 = [1]
        while a2[-1] <= c:
            if a2[-1] == c:
                return True
            a += 1
            a2.append(a*a)

        for each in a2:
            if c-each in a2:
                return True
        return False

if __name__ == "__main__":
    app = Solution()
    a = 21474826
    print(app.leetcode(a))
