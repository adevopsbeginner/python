"""

Code
Testcase
Test Result
Test Result
999. Available Captures for Rook
Easy
Topics
Companies
You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

Return the number of pawns the white rook is attacking.



Example 1:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

In this example, the rook is attacking all the pawns.

Example 2:


Input: board = [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 0

Explanation:

The bishops are blocking the rook from attacking any of the pawns.

Example 3:


Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]

Output: 3

Explanation:

The rook is attacking the pawns at positions b5, d6, and f5.



Constraints:

board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
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
    def leetcode(self, board: List[List[str]]) -> int:
        result = 0
        n = 8
        for r in range(n):
            for c in range(n):
                if board[r][c] == "R":
                    if r > 0:
                        for ii in range(r-1,-1,-1):
                            if board[ii][c] == "B":
                                break
                            if board[ii][c] == ".":
                                continue
                            if board[ii][c] == "p":
                                result += 1
                                break
                    if r < n-1:
                        for ii in range(r+1,n):
                            if board[ii][c] == "B":
                                break
                            if board[ii][c] == ".":
                                continue
                            if board[ii][c] == "p":
                                result += 1
                                break
                    if c > 0:
                        for ii in range(c-1,-1,-1):
                            if board[r][ii] == "B":
                                break
                            if board[r][ii] == ".":
                                continue
                            if board[r][ii] == "p":
                                result += 1
                                break
                    if c < n-1:
                        for ii in range(c+1,n):
                            if board[r][ii] == "B":
                                break
                            if board[r][ii] == ".":
                                continue
                            if board[r][ii] == "p":
                                result += 1
                                break

        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
