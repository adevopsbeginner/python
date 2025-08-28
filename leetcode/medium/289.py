"""
289. Game of Life
Solved
Medium
Topics
premium lock icon
Companies
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

 

Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
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
    def leetcode(self, board: List[List[int]]) -> None:

        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        change = []
        
        def eight(x,y):
            a = b = c = d = e = f = g = h = 0
            if x > 0:
                if y > 0:
                    a = board[x-1][y-1]
                b = board[x-1][y]
                if y < n-1:
                    c = board[x-1][y+1]
            if y > 0:
                d = board[x][y-1]
            if y < n-1:
                e = board[x][y+1]
            if x < m-1:
                if y > 0:
                    f = board[x+1][y-1]
                g = board[x+1][y]
                if y < n-1:
                    h = board[x+1][y+1]
            return a+b+c+d+e+f+g+h
        todie = []
        tolive = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == 0:
                    if eight(r,c) == 3:
                        tolive.append([r,c])
                else:
                    sum8 = eight(r,c)
                    if sum8 < 2:
                        todie.append([r,c])
                    elif sum8 > 3:
                        todie.append([r,c])
        for r,c in todie:
            board[r][c] = 0
        for r,c in tolive:
            board[r][c] = 1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
