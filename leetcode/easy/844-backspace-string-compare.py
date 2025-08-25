"""
844. Backspace String Compare
Easy
Topics
Companies
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
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
    def leetcode(self, s: str, t: str) -> bool:
        lls = len(s)
        ls = []
        for each in s:
            if each == "#":
                if len(ls):
                    ls.pop()
            else:
                ls.append(each)
        llt = len(t)
        lt = []
        for each in t:
            if each == "#":
                if len(lt):
                    lt.pop()
            else:
                lt.append(each)
        # print(ls,lt)

        llls = len(ls)
        lllt = len(lt)
        if llls - lllt:
            return False
        for ii in range(llls):
            if ls[ii] != lt[ii]:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
