"""
680. Valid Palindrome II
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
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
    def leetcode(self, s: str) -> bool:
        ll = len(s)
        if ll < 3:
            return True
        start = 0
        end = ll-1
        while s[start] == s[end]:
            start += 1
            end -= 1
            if start >= end-1:
                return True

        a = start+1
        b = end
        while s[a] == s[b]:
            a += 1
            b -= 1
            if a >= b-1:
                return True

        a = start
        b = end-1
        while s[a] == s[b]:
            a += 1
            b -= 1
            if a >= b-1:
                return True

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
