"""
566. Reshape the Matrix
Easy
Topics
Companies
Hint
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:

￼
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:

￼
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
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
    def leetcode(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rm = len(mat)
        if rm == 0:
            return []
        cm = len(mat[0])
        if rm == r:
            return mat

        if rm * cm - r * c:
            return mat

        # for ii in range(rm):
        #     for jj in range(cm):
        #         print(ii,jj,rm*cm)

        result = [[0 for ii in range(c)] for jj in range(r)]
        # print(result)
        for ii in range(r):
            for jj in range(c):
                ij = (ii) * c + (jj)
                # print(ii, jj, ij, ij // cm, ij % cm)
                result[ii][jj] = mat[ij // cm][ij % cm]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [[1,2],[3,4]]
    r = 4
    c = 1
    a = [[1,2,3,4]]
    r = 2
    c = 2
    print(app.leetcode(a, r, c ))
