"""
2427. Number of Common Factors
Solved
Easy
Topics
Companies
Hint
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

 

Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 

Constraints:

1 <= a, b <= 1000
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
    def leetcode(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        result = 1
        if a == b:
            up_to = a
        else:
            up_to = min(a,b,abs(b-a))
        for ii in range(1, up_to):
            if a%(ii+1) == 0 and b%(ii+1) == 0:
                result += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
