"""
1072. Flip Columns For Maximum Number of Equal Rows
Medium
Topics
Companies
Hint
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
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
    def leetcode(self, matrix: List[List[int]]) -> int:
        def allequal(r1: int, r2: int) -> bool:
            for ii in range(n):
                if matrix[r1][0] == matrix[r2][0]:
                    if matrix[r1][ii] != matrix[r2][ii]:
                        return False
                else:
                    if matrix[r1][ii] == matrix[r2][ii]:
                        return False
            return True

        m = len(matrix)
        n = len(matrix[0])
        summ = [0]*m
        for r in range(m):
            summ[r] = sum(matrix[r])
        result = 1
        for r in range(m):
            if m-r < result:
                break
            countr = 1
            for ii in range(r+1,m):
                if m-ii+countr < result:
                    break
                if allequal(r,ii):
                    countr += 1

            result = max(result,countr)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
