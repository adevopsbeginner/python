"""
1092. Shortest Common Supersequence 
Solved
Hard
Topics
Companies
Hint
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
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
    def leetcode(self, str1: str, str2: str) -> str:
        result = []
        ll1 = len(str1)
        ll2 = len(str2)

        ### 1. lcs -> dp
        dp = [[0]*(ll2+1) for _ in range(ll1+1)]
        for ii in range(1, ll1+1):
            for jj in range(1, ll2+1):
                if str1[ii-1] == str2[jj-1]:
                    dp[ii][jj] = dp[ii-1][jj-1] + 1
                else:
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])

        print(dp)

        ###2. dp -> scs
        index1 = ll1
        index2 = ll2
        while index1 > 0 and index2 > 0:
            if str1[index1-1] == str2[index2-1]:
                result.append(str1[index1-1])
                index1 -= 1
                index2 -= 1
            elif dp[index1-1][index2] > dp[index1][index2-1]:
                result.append(str1[index1-1])
                index1 -= 1
            else:
                result.append(str2[index2-1])
                index2 -= 1

        while index1 > 0:
            result.append(str1[index1-1])
            index1 -= 1
        while index2 > 0:
            result.append(str2[index2-1])
            index2 -= 1

        result = result[::-1]

        return "".join(result)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
