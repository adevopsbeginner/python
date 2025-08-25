"""

Code
Testcase
Test Result
Test Result
461. Hamming Distance
Solved
Easy
Topics
Companies
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.



Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1


Constraints:

0 <= x, y <= 231 - 1
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
    def leetcode(self, x: int, y: int) -> int:
        result = 0
        xy = x^y
        for ii in range(32):
            if xy&(1<<ii):
                result += 1
        return result

if __name__ == "__main__":
    app = Solution()
    a = 5
    b = [[1,2]]
    print(app.leetcode(a,b))
