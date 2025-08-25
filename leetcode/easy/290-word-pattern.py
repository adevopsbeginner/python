"""
290. Word Pattern
Solved
Easy
Topics
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
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
    def leetcode(self, pattern: str, s: str) -> bool:
        ls = s.split(" ")
        lp = len(pattern)
        lls = len(ls)
        if lp != lls:
            return False
        ddp = defaultdict(str)
        dds = defaultdict(str)
        for ii in range(lp):
            # print(dd,pattern[ii],ls[ii])
            if pattern[ii] in ddp:
                if ls[ii] == ddp[pattern[ii]] and pattern[ii] == dds[ls[ii]]:
                    pass
                else:
                    return False
            else:
                if ls[ii] in dds:
                    return False

                ddp[pattern[ii]] = ls[ii]
                dds[ls[ii]] = pattern[ii]
        return True

if __name__ == "__main__":
    app = Solution()
    a = "abba"
    b = "dog cat cat dog"
    print(app.leetcode(a,b))
