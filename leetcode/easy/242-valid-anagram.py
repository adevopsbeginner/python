"""
242. Valid Anagram
Solved
Easy
Topics
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, s: str, t: str) -> bool:
        ls = list(s)
        ls.sort()
        lt = list(t)
        lt.sort()
        #print(ls,lt)
        lls = len(ls)
        llt = len(lt)
        if lls != llt:
            return False
        for ii in range(lls):
            if ls[ii] != lt[ii]:
                return False
        return True

if __name__ == "__main__":
    app = Solution()
    a = [0,1,2,4,5,7]
    print(app.leetcode(a))
