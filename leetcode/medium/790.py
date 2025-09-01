"""
790. Domino and Tromino Tiling
Medium
Topics
premium lock icon
Companies
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are shown above.
Example 2:

Input: n = 1
Output: 1
 

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
        ### chatgpt
        MOD = 10**9 + 7
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        
        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
        
        return dp[n]

        ### my wrong answer, no sticking out section considered
        nn = [1]*(max(4, n+1))
        nn[1] = 1
        nn[2] = 2
        nn[3] = 5

        if n < 4:
            return nn[n]
        
        for ii in range(4, n+1):
            nn[ii] = nn[ii-3]*2 + nn[ii-2] + nn[ii-1]

        return nn[n] % (10**9+7)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
