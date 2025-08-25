"""
344. Reverse String
Solved
Easy
Topics
Companies
Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
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
    def leetcode(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ll = len(s)
        for ii in range(ll//2):
            c = s[ii]
            s[ii],s[ll-1-ii] = s[ll-1-ii],s[ii]

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    print(app.leetcode(a))
