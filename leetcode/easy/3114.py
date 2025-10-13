"""
3114. Latest Time You Can Obtain After Replacing Characters
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s representing a 12-hour format time where some of the digits (possibly none) are replaced with a "?".

12-hour times are formatted as "HH:MM", where HH is between 00 and 11, and MM is between 00 and 59. The earliest 12-hour time is 00:00, and the latest is 11:59.

You have to replace all the "?" characters in s with digits such that the time we obtain by the resulting string is a valid 12-hour format time and is the latest possible.

Return the resulting string.

 

Example 1:

Input: s = "1?:?4"

Output: "11:54"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "11:54".

Example 2:

Input: s = "0?:5?"

Output: "09:59"

Explanation: The latest 12-hour format time we can achieve by replacing "?" characters is "09:59".

 

Constraints:

s.length == 5
s[2] is equal to the character ":".
All characters except s[2] are digits or "?" characters.
The input is generated such that there is at least one time between "00:00" and "11:59" that you can obtain after replacing the "?" characters.
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
        h1 = s[0]
        h2 = s[1]
        m1 = s[3]
        m2 = s[4]
        if s[0:2] == "??":
            h1 = "1"
            h2 = "1"
        elif h1 == "?":
            if h2 in "01":
                h1 = "1"
            else:
                h1 = "0"
        elif h2 == "?":
            if h1 == "1":
                h2 = "1"
            else:
                h2 = "9"

        if s[3:] == "??":
            m1 = "5"
            m2 = "9"
        elif m1 == "?":
            m1 = "5"
        elif m2 == "?":
            m2 = "9"
        
        return h1+h2+":"+m1+m2


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
