"""
739. Daily Temperatures
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
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
    def leetcode(self, temperatures: List[int]) -> List[int]:
        ll = len(temperatures)
        result = [0]*ll
        q = [[temperatures[0], 0]]
        heapq.heapify(q)
        for ii in range(1,ll):
            heapq.heappush(q,[temperatures[ii], ii])
            while len(q):
                p,index = heapq.heappop(q)
                #print(p, index,q, ii, temperatures[ii])
                if p < temperatures[ii]:
                    result[index] = ii-index
                else:
                    heapq.heappush(q,[p,index])
                    break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
