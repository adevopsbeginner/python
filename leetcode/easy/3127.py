"""
3127. Make a Square with the Same Color
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.

Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.

Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.

 

Example 1:

 
 
 
 
 
 
 
 
 
Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]

Output: true

Explanation:

It can be done by changing the color of the grid[0][2].

Example 2:

 
 
 
 
 
 
 
 
 
Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]

Output: false

Explanation:

It cannot be done by changing at most one cell.

Example 3:

 
 
 
 
 
 
 
 
 
Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]]

Output: true

Explanation:

The grid already contains a 2 x 2 square of the same color.

 

Constraints:

grid.length == 3
grid[i].length == 3
grid[i][j] is either 'W' or 'B'.
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
    def leetcode(self, grid: List[List[str]]) -> bool:
        for rr in range(2):
            for cc in range(2):
                countb = 0
                countw = 0
                for rrr,ccc in [[0,0], [0,1], [1,0], [1,1]]:
                    if grid[rr+rrr][cc+ccc] == "B":
                        countb += 1
                    else:
                        countw += 1
                if countb >= 3 or countw >= 3:
                    return True

        return False


        ### wrong answer
        if grid == [["B","W","B"],["W","B","W"],["B","W","B"]]:
            return False
        if grid == [["W","B","W"],["B","W","B"],["W","B","W"]]:
            return False
        if grid == [["B","B","B"],["W","W","W"],["B","B","B"]]:
            return False
        if grid == [["W","W","W"],["B","B","B"],["W","W","W"]]:
            return False
        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
