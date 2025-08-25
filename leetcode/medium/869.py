"""
869. Reordered Power of 2
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
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
    def leetcode(self, n: int) -> bool:
        power_of_two = ["1"]
        pot = 1
        while pot < 1000000000:
            pot *= 2
            strpot = str(pot)
            listpot = list(strpot)
            listpot.sort()
            strpot2 = "".join(listpot)
            power_of_two.append(strpot2)
        
        strn = str(n)
        listn = list(strn)
        listn.sort()
        strn2 = "".join(listn)
        
        if strn2 in power_of_two:
            return True
        
        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
