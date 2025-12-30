"""
840. Magic Squares In Grid
Solved
Medium
Topics
premium lock icon
Companies
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[int]]) -> int:
        def is_5_in_surroundings(rr,cc):
            digits = []
            digits += [grid[rr-1][cc-1], grid[rr-1][cc], grid[rr-1][cc+1]]
            digits += [grid[rr][cc-1], grid[rr][cc+1]]
            digits += [grid[rr+1][cc-1], grid[rr+1][cc], grid[rr+1][cc+1]]

            if 5 in digits:
                return True

            return False
                    
        def are_they_1_to_9(rr,cc):
            digits = [5]
            digits += [grid[rr-1][cc-1], grid[rr-1][cc], grid[rr-1][cc+1]]
            digits += [grid[rr][cc-1], grid[rr][cc+1]]
            digits += [grid[rr+1][cc-1], grid[rr+1][cc], grid[rr+1][cc+1]]
            if sorted(digits) == [1,2,3,4,5,6,7,8,9]:
                return True
            return False
                    
        def sum_10(rr,cc):
            if grid[rr-1][cc-1]+grid[rr+1][cc+1] != 10:
                #print(41)
                return False
            if grid[rr-1][cc]+grid[rr+1][cc] != 10:
                #print(42)
                return False
            if grid[rr-1][cc+1]+grid[rr+1][cc-1] != 10:
                #print(43)
                return False
            if grid[rr][cc-1]+grid[rr][cc+1] != 10:
                #print(44)
                return False
            if grid[rr-1][cc-1]+ grid[rr-1][cc]+ grid[rr-1][cc+1] != 15:
                return False
            if grid[rr+1][cc-1]+ grid[rr+1][cc]+ grid[rr+1][cc+1] != 15:
                return False
            if grid[rr-1][cc-1]+ grid[rr][cc-1]+ grid[rr+1][cc-1] != 15:
                return False
            if grid[rr-1][cc+1]+ grid[rr][cc+1]+ grid[rr+1][cc+1] != 15:
                return False

            return True

        result = 0
        m = len(grid)
        n = len(grid[0])
        for rr in range(1,m-1):
            for cc in range(1, n-1):
                if grid[rr][cc] != 5:
                    #print(111)
                    continue
                if is_5_in_surroundings(rr,cc):
                    #print(222)
                    continue
                if not are_they_1_to_9(rr,cc):
                    #print(333)
                    continue
                if not sum_10(rr,cc):
                    #print(444)
                    continue
                result += 1

        return result
