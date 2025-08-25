"""
1504. Count Submatrices With All Ones
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

 

Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
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

        result = 0

        ### 1
        for rr in range(m-1, -1, -1):
            for cc in range(n-1, -1, -1):
                if mat[rr][cc] == 0:
                    mat[rr][cc] = [0, 0]
                    continue

                right1 = 1
                if cc  < n-1:
                    right1 += mat[rr][cc+1][1]

                mat[rr][cc] = [1, right1]

        #print(mat)
        
        ### 2 loop
        for rr in range(m):
            for cc in range(n):
                ### 3 addup
                right_count = mat[rr][cc][1]
                for ii in range(rr, m):
                    if mat[ii][cc][0] == 1:
                        right_count = min(right_count, mat[ii][cc][1])
                        result += right_count
                    else:
                        break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
