"""
1190. Reverse Substrings Between Each Pair of Parentheses
Medium
Topics
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.



Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
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
        ll = len(s)
        copy = s
        while "(" in copy:
            right = 0
            left = 0
            while copy[right] != ")":
                # print(left,right, copy)
                right += 1
            left = right
            while copy[left] != "(":
                left -= 1
            tail = ""
            if right + 1 < ll:
                tail = copy[right + 1:]
            copy = copy[:left] + copy[right-1:left:-1] + tail
        return copy


if __name__ == "__main__":
    app = Solution()
    a = "ab(cd)"
    a = "(u(love)i)"
    print(app.leetcode(a))
