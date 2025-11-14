"""
2536. Increment Submatrices by One
Medium
Topics
premium lock icon
Companies
Hint
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:

1 <= n <= 500
1 <= queries.length <= 104
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ### 2D diff
        result = [[0]*(n+1) for _ in range(n+1)]

        for r1,c1,r2,c2 in queries:
            result[r1][c1] += 1
            result[r1][c2+1] -= 1
            result[r2+1][c1] -= 1
            result[r2+1][c2+1] += 1

        ### 2D prefix sum
        for rr in range(n):
            for cc in range(n):
                if rr > 0:
                    result[rr][cc] += result[rr-1][cc]
                if cc > 0:
                    result[rr][cc] += result[rr][cc-1]
                if rr > 0 and cc > 0:
                    result[rr][cc] -= result[rr-1][cc-1]


        return [row[:n] for row in result[:n]]

        ### linear diff, wrong answer with bug
        result = [[0]*n for _ in range(n)]

        for r1,c1,r2,c2 in queries:
            if c1 == 0 and c2 == n-1:
                result[r1][0] += 1
                if r2 < n-1:
                    result[r2+1][0] -= 1
                continue

            for rr in range(r1, r2+1):
                result[rr][c1] += 1
                if c2+1 == n:
                    if rr+1 < n:
                        result[rr+1][c1-1] -= 1
                else:
                    print(rr, r1,c1, r2,c2)
                    result[rr][c2+1] -= 1

        print(result)

        base = 0
        for rr in range(n):
            for cc in range(n):
                result[rr][cc] += base
                base = result[rr][cc]

        return result
