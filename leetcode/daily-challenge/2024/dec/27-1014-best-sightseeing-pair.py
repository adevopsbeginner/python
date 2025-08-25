"""
1014. Best Sightseeing Pair
Medium
Topics
Companies
Hint
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
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
    def leetcode(self, values: List[int]) -> int:
        ll = len(values)
        result = values[0]+values[1]-1
        maxii = values[0]
        maxv = max(values)

        for ii in range(1,ll):
            values[ii] -= ii
        result = values[0]+max(values[1:])
        for ii in range(1,ll):
            values[ii] += ii

        for ii in range(ll):
            if values[ii]+ii <= maxii:
                continue
            maxii = values[ii]+ii

            for jj in range(ii+1,min(ll,ii+maxv*2)):
                result = max(result,values[ii]+values[jj]+ii-jj)

        return result

        ### time limit exceeded, 45/55
        for ii in range(ll):
            if values[ii]+ii < maxii:
                continue
            maxii = values[ii]+ii

            for jj in range(ii+1,min(ll,ii+2000)):
                result = max(result,values[ii]+values[jj]+ii-jj)

        return result
        
        ### memory limit exceeded, 42/55
        matrix = [[0 for _ in range(ll)] for _ in range(ll)]
        for rr in range(ll):
            for cc in range(rr+1,ll):
                matrix[rr][cc] = values[rr] + values[cc] + (rr-cc)

        for rr in range(ll):
            for cc in range(rr+1, ll):
                if matrix[rr][cc] > result:
                    result = matrix[rr][cc]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
