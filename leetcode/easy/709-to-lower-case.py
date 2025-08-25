"""
709. To Lower Case
Easy
Topics
Companies
Hint
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
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
        ls = list(s)
        #print(ls)
        ll = len(ls)
        for ii in range(ll):
            if ls[ii] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                ls[ii] = chr(ord('a') + ord(ls[ii]) - ord('A'))

        return "".join(ls)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
