"""
50. Pow(x, n)
Solved
Medium
Topics
premium lock icon
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
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
    def leetcode(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        flag = 0
        if n < 0:
            n = 0-n
            flag = 1
        p = 1
        p32 = [x]
        for ii in range(1,32):
            p32.append(p32[ii-1]*p32[ii-1])
        for ii in range(32):
            y = 1<<ii
            if n&y:
                p *= p32[ii]
            
        if flag:
            p = 1/p
        
        return p


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
