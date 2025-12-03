"""
3407. Substring Matching Pattern
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s and a pattern string p, where p contains exactly one '*' character.

The '*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a substring of s, and false otherwise.

 

Example 1:

Input: s = "leetcode", p = "ee*e"

Output: true

Explanation:

By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:

Input: s = "car", p = "c*v"

Output: false

Explanation:

There is no substring matching the pattern.

Example 3:

Input: s = "luck", p = "u*"

Output: true

Explanation:

The substrings "u", "uc", and "uck" match the pattern.

 

Constraints:

1 <= s.length <= 50
1 <= p.length <= 50 
s contains only lowercase English letters.
p contains only lowercase English letters and exactly one '*'
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
    def leetcode(self, s: str, p: str) -> bool:
        lls = len(s)
        llp = len(p)
        for ii in range(llp):
            if p[ii] == "*":
                p1 = p[0:ii]
                p1ll = ii
                p2 = p[ii+1:]
                p2ll = llp-ii-1
        #print(p1,p1ll,p2,p2ll)
        if p1 not in s:
            return False
        if p2 not in s:
            return False
        for ii in range(lls):
            if s[ii:ii+p1ll] == p1:
                #print(ii)
                if p2 == "":
                    return True
                    
                if p2 not in s[ii+p1ll:]:
                    return False
                for jj in range(ii+p1ll,lls):
                    if s[jj:jj+p2ll] == p2:
                        return True
        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
