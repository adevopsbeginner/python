"""
1140. Stone Game II
Medium
Topics
Companies
Hint
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104


Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
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
    def leetcode(self, piles: List[int]) -> int:
        ### chatgpt
        n = len(piles)

        # Calculate suffix sums
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # dp[i][m] means the maximum stones Alice can get starting from i with M = m
        dp = [[0] * (n + 1) for _ in range(n+1)]

        # Fill the dp table
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                # Alice can take at most the first 2 * m piles
                for x in range(1, 2 * m + 1):
                    if i + x <= n:
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])

        return dp[0][1]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
