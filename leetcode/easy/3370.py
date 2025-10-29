"""
3370. Smallest Number With All Set Bits
Solved
Easy
Topics
￼
Companies
Hint
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only ￼set bits

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

1 <= n <= 1000
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
    def leetcode(self, n: int) -> int:
        for ii in range(32):
            if 1<<ii > n:
                return (1<<ii)-1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
