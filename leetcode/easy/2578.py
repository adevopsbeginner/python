"""
2578. Split With Minimum Sum
Easy
Topics
premium lock icon
Companies
Hint
Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.
 

Example 1:

Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
Example 2:

Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.
 

Constraints:

10 <= num <= 109
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
        lnum = list(str(num))
        lnum.sort()
        num1 = 0
        num2 = 0
        ll = len(lnum)
        for ii in range(ll):
            if ii%2 == 0:
                num1 = num1*10 + int(lnum[ii])
            else:
                num2 = num2*10 + int(lnum[ii])
        
        return num1 + num2

        ### wrong answer
        ### does not have to be in order
        strnum = str(num)
        ll = len(strnum)
        result = num
        for ii in range(ll-1):
            num1 = int(strnum[0:ii+1])
            num2 = int(strnum[ii+1:])
            #print(strnum, ii, num1, num2, num1+num2)
            result = min(result, num1+num2)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
