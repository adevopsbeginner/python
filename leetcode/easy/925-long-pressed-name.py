"""
925. Long Pressed Name
Easy
Topics
Companies
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
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
    def leetcode(self, name: str, typed: str) -> bool:
        iname = 0
        lln = len(name)
        ityped = 0
        llt = len(typed)
        while iname < lln:
            print(111,iname,name[iname], ityped,typed[ityped])
            if name[iname] != typed[ityped]:
                if iname == 0:
                    return False
                while ityped < llt and typed[ityped] == typed[ityped-1]:
                    ityped += 1
                    if ityped == llt:
                        return False
                #print(222,iname,name[iname], ityped,typed[ityped])
                if name[iname] != typed[ityped]:
                    return False
            iname += 1
            ityped += 1
            if ityped == llt and iname < lln:
                return False

        while ityped < llt:
            if typed[ityped] != typed[ityped-1]:
                return False
            ityped += 1

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
