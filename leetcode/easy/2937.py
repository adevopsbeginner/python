"""
2937. Make Three Strings Equal
Easy
Topics
premium lock icon
Companies
Hint
You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.

Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.

 

Example 1:

Input: s1 = "abc", s2 = "abb", s3 = "ab"

Output: 2

Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.

Example 2:

Input: s1 = "dac", s2 = "bac", s3 = "cac"

Output: -1

Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.

 

Constraints:

1 <= s1.length, s2.length, s3.length <= 100
s1, s2 and s3 consist only of lowercase English letters.
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
    def leetcode(self, s1: str, s2: str, s3: str) -> int:
        ll1 = len(s1)
        ll2 = len(s2)
        ll3 = len(s3)
        minll = min(ll1, ll2, ll3)
        if s1[0:minll] == s2[0:minll] == s3[0:minll]:
            return ll1+ll2+ll3-minll*3

        result = -1
        if s1[0] == s2[0] == s3[0]:
            for ii in range(1, min(ll1, ll2, ll3)):
                if s1[ii] == s2[ii] == s3[ii]:
                    continue
                result = ll1-ii+ll2-ii+ll3-ii
                break
            
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
