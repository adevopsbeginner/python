"""
2566. Maximum Difference by Remapping a Digit
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108
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
    def leetcode(self, num: int) -> int:
        remax = 0
        remin = 0
        int2list = []
        while num:
            int2list = [num%10] + int2list
            num //= 10

        ll = len(int2list)
        
        to_replace = -1
        for ii in range(ll):
            if int2list[ii] == 9:
                remax = remax*10 + 9
            elif to_replace == -1:
                to_replace = int2list[ii]
                remax = remax*10 + 9
            elif to_replace == int2list[ii]:
                remax = remax*10 + 9
            else:
                remax = remax*10 + int2list[ii]
            
        to_replace = int2list[0]
        for ii in range(ll):
            if to_replace == int2list[ii]:
                remin = remin*10 + 0
            else:
                remin = remin*10 + int2list[ii]

        return remax-remin


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
