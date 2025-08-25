"""
72. Edit Distance
Solved
Medium
Topics
premium lock icon
Companies
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
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
    def leetcode(self, word1: str, word2: str) -> int:
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = '0'+word1
        w2 = '0'+word2
        lw1 = len(w1)
        lw2 = len(w2)

        dp = [ [0 for ii in range(lw2)] for jj in range(lw1)]

        for ii in range(lw1):
            dp[ii][0] = ii

        for ii in range(lw2):
            dp[0][ii] = ii

        for ii in range(1,lw1):
            for jj in range(1,lw2):
                if w1[ii] == w2[jj]:
                    cost = 0
                else:
                    cost = 1
                dp[ii][jj] = min(dp[ii-1][jj]+1,dp[ii][jj-1]+1,dp[ii-1][jj-1]+cost)

        #print(dp)

        return dp[-1][-1]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
