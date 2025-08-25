"""
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
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
        result = ""
        ll1 = len(str1)
        ll2 = len(str2)
        llr = 0
        index = 0
        llmin = min(ll1,ll2)
        for ii in range(1,llmin+1):
            if llmin%ii:
                continue
            llminii = llmin // ii
            if ll1%llminii:
                continue
            if ll2%llminii:
                continue
            if str1[:llminii] != str2[:llminii]:
                return ""
            if str1[:llminii]*(ll1//llminii) != str1:
                continue
            if str2[:llminii]*(ll2//llminii) != str2:
                continue
            return str1[:llminii]

        return ""


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
