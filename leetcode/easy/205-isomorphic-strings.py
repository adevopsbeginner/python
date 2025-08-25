'''
205. Isomorphic Strings
Solved
Easy
Topics
Companies
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

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
        sdd = defaultdict()
        tdd = defaultdict()
        ll = len(s)
        for ii in range(ll):
            if s[ii] in sdd and t[ii] in tdd:
                if sdd[s[ii]] == t[ii] and tdd[t[ii]] == s[ii]:
                    continue
                else:
                    return False
            elif s[ii] in sdd or t[ii] in tdd:
                return False

            sdd[s[ii]] = t[ii]
            tdd[t[ii]] = s[ii]
        return True

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
