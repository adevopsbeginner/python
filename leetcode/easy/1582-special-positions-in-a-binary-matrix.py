"""
1582. Special Positions in a Binary Matrix
Solved
Easy
Topics
Companies
Hint
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:


Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:


Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
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
    def leetcode(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        sum_r = [0]*m
        sum_c = [0]*n
        for ii in range(m):
            for jj in range(n):
                sum_r[ii] += mat[ii][jj]
                sum_c[jj] += mat[ii][jj]

        result = 0
        for ii in range(m):
            for jj in range(n):
                if mat[ii][jj] == 1 and sum_r[ii] == 1 and sum_c[jj] == 1:
                    result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
