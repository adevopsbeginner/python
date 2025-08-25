"""
507. Perfect Number
Easy
Topics
Companies
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.



Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false


Constraints:

1 <= num <= 108
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
    def leetcode(self, num: int) -> bool:
        divisors = [1]
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        print(divisors)

        return num == sum(divisors)


if __name__ == "__main__":
    app = Solution()
    a = 28
    print(app.leetcode(a))
