"""
120. Triangle
Medium
Topics
premium lock icon
Companies
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
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
    def leetcode(self, triangle: List[List[int]]) -> int:
        level = len(triangle)
        for rr in range(level-2,-1,-1):
            for cc in range(len(triangle[rr])):
                triangle[rr][cc] += min(triangle[rr+1][cc], triangle[rr+1][cc+1])
        return triangle[0][0]

        ### time limit exceeded
        level = len(triangle)
        result = 100000
        q = [[0,0,0]]
        while q:
            rr,cc,path_sum = q.pop()
            if rr == level-1:
                result = min(result, path_sum+triangle[rr][cc])
                continue
            q.append([rr+1,cc+1,path_sum+triangle[rr][cc]])
            q.append([rr+1,cc,path_sum+triangle[rr][cc]])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
