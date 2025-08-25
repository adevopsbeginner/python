"""
504. Base 7
Easy
Topics
Companies
Given an integer num, return a string of its base 7 representation.



Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


Constraints:

-107 <= num <= 107
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
    def leetcode(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = ""
        if num < 0:
            sign = "-"
            num = 0-num
        result = ""
        while num:
            remainder = num%7
            result = str(remainder) + result
            num //= 7

        return sign + result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
