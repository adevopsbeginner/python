"""
1331. Rank Transform of an Array
Easy
Topics
Companies
Hint
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.


Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]


Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
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
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dd = defaultdict(int)
        ll = len(arr)
        for ii in range(ll):
            dd[arr[ii]] = 0
        ldd = []
        for each in dd:
            ldd.append([each,dd[each]])
        ldd.sort()
        #print(ldd)
        llldd = len(ldd)
        for ii in range(llldd):
            ldd[ii][1] = ii+1
        #print(ldd)
        ddd = dict(ldd)
        # for each in ddd:
        #     print(each,ddd[each])
        result = [0]*ll
        for ii in range(ll):
            result[ii] = ddd[arr[ii]]
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
