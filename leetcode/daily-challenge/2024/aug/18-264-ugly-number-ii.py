"""

Code
Testcase
Test Result
Test Result
264. Ugly Number II
Solved
Medium
Topics
Companies
Hint
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:

1 <= n <= 1690
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
        ### chatgpt
        ugly = [0] * n
        ugly[0] = 1

        i2 = i3 = i5 = 0

        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly

            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2

            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3

            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5

        return ugly[-1]

        result = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12] + [0] * 1690
        return result[n]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
