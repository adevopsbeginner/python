"""
37. Sudoku Solver
Solved
Hard
Topics
premium lock icon
Companies
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
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
        ### chatgpt
        # Bitmasks for used digits in each row/col/box (1 bit per digit 1..9)
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9
        empties = []

        def bid(i, j):
            return (i // 3) * 3 + (j // 3)

        # Initialize masks and list of empty cells
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empties.append((i, j))
                else:
                    b = 1 << (ord(ch) - ord('1'))
                    row[i] |= b
                    col[j] |= b
                    box[bid(i, j)] |= b

        ALL = (1 << 9) - 1  # 0b111111111

        def dfs(k: int = 0) -> bool:
            if k == len(empties):
                return True

            # Choose the cell with the fewest candidates among positions k..end
            best = -1
            best_mask = 0
            best_cnt = 10
            for t in range(k, len(empties)):
                i, j = empties[t]
                m = ALL ^ (row[i] | col[j] | box[bid(i, j)])  # candidates mask
                c = m.bit_count()
                if c < best_cnt:
                    best_cnt, best, best_mask = c, t, m
                    if c == 1:
                        break
            if best_cnt == 0:
                return False

            # Place the chosen cell at position k (stable order via swap)
            empties[k], empties[best] = empties[best], empties[k]
            i, j = empties[k]
            b_id = bid(i, j)
            mask = best_mask if best == k else (ALL ^ (row[i] | col[j] | box[b_id]))

            # Try each candidate (iterate low bits)
            while mask:
                bit = mask & -mask
                d = bit.bit_length()          # 1..9
                ch = str(d)

                board[i][j] = ch
                row[i] |= bit
                col[j] |= bit
                box[b_id] |= bit

                if dfs(k + 1):
                    return True

                # undo
                board[i][j] = '.'
                row[i] &= ~bit
                col[j] &= ~bit
                box[b_id] &= ~bit

                mask -= bit

            # restore (optional cleanup; not strictly required)
            empties[k], empties[best] = empties[best], empties[k]
            return False

        dfs()


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
