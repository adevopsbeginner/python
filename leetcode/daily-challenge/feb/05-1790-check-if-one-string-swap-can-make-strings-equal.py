"""
1790. Check if One String Swap Can Make Strings Equal
Solved
Easy
Topics
Companies
Hint
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
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
    def leetcode(self, s1: str, s2: str) -> bool:
        ll = len(s1)
        count = 0
        i1 = -1
        i2 = -1
        for ii in range(ll):
            if s1[ii] != s2[ii]:
                if count == 0:
                    i1 = ii
                    count = 1
                elif count == 1:
                    i2 = ii
                    count = 2
                else:
                    return False
        if i2 >= 0:
            if s1[i1] == s2[i2] and s1[i2] == s2[i1]:
                return True
            else:
                return False
        elif i1 >= 0:
            return False
        
        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
