"""
2787. Ways to Express an Integer as Sum of Powers
Medium
Topics
premium lock icon
Companies
Hint
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
 

Constraints:

1 <= n <= 300
1 <= x <= 5
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
    def leetcode(self, n: int, x: int) -> int:
        @lru_cache(None)
        def dp(start,n, result):
            for ii in range(start,n+1):
                iix = ii**x
                if iix > n:
                    return result
                if iix == n:
                    return result+1
                result = dp(ii+1, n-iix, result)

            return result

        if x > 1:
            result = dp(1, n, 0)
            return result

        ### I asked chatgpt
        powers = [ii for ii in range(1, n+1)]

        dp = [0]*(n+1)
        dp[0] = 1

        for each in powers:
            for ii in range(n,each-1,-1):
                dp[ii] = dp[ii]+dp[ii-each]

        return dp[n] % 1000000007



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
