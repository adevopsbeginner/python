"""
5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
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
    def leetcode(self, s: str) -> str:
        def palindromic(start: int, end: int) -> bool:
            while end > start:
                if s[end] != s[start]:
                    return False
                start += 1
                end -= 1
            return True

        ll = len(s)
        result = s[0]
        for ii in range(ll):
            for jj in range(ll-1,ii,-1):
                if palindromic(ii,jj):
                    if jj-ii+1 > len(result):
                        result = s[ii:jj+1]
                    break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
