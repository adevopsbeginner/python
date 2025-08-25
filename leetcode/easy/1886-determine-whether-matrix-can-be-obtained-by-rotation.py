"""
1886. Determine Whether Matrix Can Be Obtained By Rotation
Solved
Easy
Topics
Companies
Hint
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
 

Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.
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
    def leetcode(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        r0 = True
        r1 = True
        r2 = True
        r3 = True
        for rr in range(n):
            for cc in range(n):
                if mat[rr][cc] != target[rr][cc]:
                    r0 = False
                    break
        for rr in range(n):
            for cc in range(n):
                #print(rr,cc,cc,)
                if mat[rr][cc] != target[cc][n-1-rr]:
                    r1 = False
                    break
        for rr in range(n):
            for cc in range(n):
                #print(rr,cc,cc,)
                if mat[rr][cc] != target[n-1-rr][n-1-cc]:
                    r2 = False
                    break
        for rr in range(n):
            for cc in range(n):
                #print(rr,cc,cc,)
                if mat[rr][cc] != target[n-1-cc][rr]:
                    r3 = False
                    break
        print(r1,r2,r3)
        return r0 or r1 or r2 or r3


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
