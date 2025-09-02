"""
79. Word Search
Solved
Medium
Topics
premium lock icon
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
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
    def leetcode(self, board: List[List[str]], word: str) -> bool:
        lw = len(word)
        if lw == 0:
            return True

        lr = len(board)
        if lr == 0:
            return False

        lc = len(board[0])
        if lc == 0:
            return False
        
        def dfs(r,c,word):
            #print(r,c,word,flag)
            if len(word) == 0:
                return True
            #print(word[0])
            if board[r][c] != word[0]:
                return False
            if len(word) == 1:
                return True

            #print(r,c, board,word)

            board[r][c] = "#"

            if r > 0 and board[r-1][c] == word[1]:
                if dfs(r-1,c,word[1:]):
                    board[r][c] = word[0]
                    return True
            if r < lr-1 and board[r+1][c] == word[1]:
                if dfs(r+1,c,word[1:]):
                    board[r][c] = word[0]
                    return True
            if c > 0 and board[r][c-1] == word[1]:
                if dfs(r,c-1,word[1:]):
                    board[r][c] = word[0]
                    return True
            if c < lc-1 and board[r][c+1] == word[1]:
                if dfs(r,c+1,word[1:]):
                    board[r][c] = word[0]
                    return True
            
            board[r][c] = word[0]
                
            return False
        
        for r in range(lr):
            for c in range(lc):
                if board[r][c] == word[0]:
                    if dfs(r,c,word):
                        return True

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
