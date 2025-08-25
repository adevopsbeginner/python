"""
415. Add Strings
Easy
Topics
Companies
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
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
    def leetcode(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return num2
        if num2 == '0':
            return num1

        ll1 = len(num1)
        ll2 = len(num2)
        result = ""
        nc = 0
        for ii in range(max(ll1,ll2)):
            # print(ii,num1[-1-ii], num2[-1-ii])
            if ii >= ll1:
                i1 = 0
            else:
                i1 = ord(num1[-1-ii])-ord('0')

            if ii >= ll2:
                i2 = 0
            else:
                i2 = ord(num2[-1-ii])-ord('0')
            # print(ii,i1,i2,nc,result)

            result = str((i1+i2+nc)%10)+result
            nc = (i1+i2+nc)//10

        if nc:
            result = '1'+result

        return result

if __name__ == "__main__":
    app = Solution()
    a = "11"
    b = "123"
    print(app.leetcode(a,b))
