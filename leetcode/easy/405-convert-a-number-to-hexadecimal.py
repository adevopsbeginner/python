"""
405. Convert a Number to Hexadecimal
Easy
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.



Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"


Constraints:

-231 <= num <= 231 - 1
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
    def leetcode(self, num: int) -> str:
        result = ""
        hexc = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for ii in range(8):
            #print(num,result)
            result = hexc[num & 0xf]+result
            num >>= 4
        for ii in range(8):
            #print(result,result[ii])
            if result[ii] != '0':
                return result[ii:]

        return "0"

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    a = 100000
    print(app.leetcode(a))
