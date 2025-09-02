"""
2843. Count Symmetric Integers
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given two positive integers low and high.

An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

Return the number of symmetric integers in the range [low, high].

 

Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 

Constraints:

1 <= low <= high <= 104
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
    def leetcode(self, low: int, high: int) -> int:
        result = 0
        for ii in range(low, high+1):
            tostr = str(ii)
            ll = len(tostr)
            if ll % 2 == 1:
                continue
            tolist = list(tostr)
            for jj in range(ll):
                tolist[jj] = int(tolist[jj])
            #print(ii, sum(tolist[0:ll//2]), sum(tolist))
            if sum(tolist[0:ll//2])*2 == sum(tolist):
                result += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
