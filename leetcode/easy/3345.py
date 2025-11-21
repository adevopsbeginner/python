"""
3345. Smallest Divisible Digit Product I
Easy
Topics
premium lock icon
Companies
Hint
You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

 

Constraints:

1 <= n <= 100
1 <= t <= 10
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
    def leetcode(self, n: int, t: int) -> int:
        if n == 100:
            return 100

        for ii in range(11):
            if "0" in str(n+ii):
                return n+ii
            product = (n+ii)%10
            if n+ii >= 10:
                product *= (n+ii)//10
            if product%t == 0:
                return n+ii
        return n


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
