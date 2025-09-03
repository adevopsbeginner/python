"""
54. Spiral Matrix
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
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
    def leetcode(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = [0]*(m*n)
        rr = 0
        cc = 0
        direction = 1
        for ii in range(m*n):
            #print(rr,cc,matrix[rr][cc], direction)
            result[ii] = matrix[rr][cc]
            matrix[rr][cc] = -1000
            if direction == 1:
                if cc == n-1:
                    direction = 2
                    rr += 1
                elif matrix[rr][cc+1] == -1000:
                    direction = 2
                    rr += 1
                else:
                    cc += 1
            elif direction == 2:
                if rr == m-1:
                    direction = 3
                    cc -= 1
                elif matrix[rr+1][cc] == -1000:
                    direction = 3
                    cc -= 1
                else:
                    rr += 1
            elif direction == 3:
                if cc == 0:
                    direction = 4
                    rr -= 1
                elif matrix[rr][cc-1] == -1000:
                    direction = 4
                    rr -= 1
                else:
                    cc -= 1
            elif direction == 4:
                if rr == 0:
                    direction = 1
                    cc += 1
                elif matrix[rr-1][cc] == -1000:
                    direction = 1
                    cc += 1
                else:
                    rr -= 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
