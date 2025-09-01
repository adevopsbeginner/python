"""
130. Surrounded Regions
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
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
    def leetcode(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lr = len(board)
        if lr == 0:
            return
        lc = len(board[0])
        no = [[0 for cc in range(lc)] for rr in range(lr)]
        #print(no)
        def dfs(r,c):
            if no[r][c]:
                return
            no[r][c] = 1
            if r > 0 and board[r-1][c] == 'O':
                dfs(r-1,c)
            if r < lr-1 and board[r+1][c] == 'O':
                dfs(r+1,c)
            if c > 0 and board[r][c-1] == 'O':
                dfs(r,c-1)
            if c < lc-1 and board[r][c+1] == 'O':
                dfs(r,c+1)
                
        for rr in range(lr):
            if board[rr][0] == 'O':
                dfs(rr,0)
            if board[rr][lc-1] == 'O':
                dfs(rr,lc-1)
                
        for cc in range(lc):
            if board[0][cc] == 'O':
                dfs(0,cc)
            if board[lr-1][cc] == 'O':
                dfs(lr-1,cc)
                
        #print(no)
                
        for rr in range(lr):
            for cc in range(lc):
                if no[rr][cc] == 0 and board[rr][cc] == 'O':
                    board[rr][cc] = 'X'


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
