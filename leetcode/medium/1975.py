"""
1975. Maximum Matrix Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        themin = abs(matrix[0][0])
        result = 0
        count = 0
        for rr in range(n):
            for cc in range(n):
                result += abs(matrix[rr][cc])
                themin = min(themin, abs(matrix[rr][cc]))
                
                if matrix[rr][cc] < 0:
                    count += 1

        if count%2:
            result -= 2*abs(themin)

        return result
