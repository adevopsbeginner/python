"""
2133. Check if Every Row and Column Contains All Numbers
Easy
Topics
Companies
Hint
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

 

Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
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
    def leetcode(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for rr in range(n):
            if min(matrix[rr]) != 1:
                return False
            if max(matrix[rr]) != n:
                return False
            if len(set(matrix[rr])) != n:
                return False

        for cc in range(n):
            column = [matrix[rr][cc] for rr in range(n)]
            if min(column) != 1:
                return False
            if max(column) != n:
                return False
            if len(set(column)) != n:
                return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
