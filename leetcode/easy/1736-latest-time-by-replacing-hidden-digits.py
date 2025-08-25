"""
1736. Latest Time by Replacing Hidden Digits
Solved
Easy
Topics
Companies
Hint
You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"
 

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
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
    def leetcode(self, time: str) -> str:
        d1 = "2"
        d2 = "9"
        d3 = "5"
        d4 = "9"

        if time[0] in "01":
            d1 = time[0]
        else:
            if time[1] in "456789":
                d1 = "1"

        if time[1] in "0123456789":
            d2 = time[1]
        else:
            if d1 == "2":
                d2 = "3"

        if time[3] in "0123456789":
            d3 = time[3]

        if time[4] in "0123456789":
            d4 = time[4]
        
        return d1+d2+":"+d3+d4


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
