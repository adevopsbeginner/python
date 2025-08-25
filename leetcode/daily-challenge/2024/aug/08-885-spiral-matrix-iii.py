"""
885. Spiral Matrix III
Medium
Topics
Companies
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.



Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
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
    def leetcode(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        half = max(rStart-0+1,rows-rStart, cStart-0+1, cols-cStart)
        mr = half
        mc = half-1
        rStart += 1

        matrix = [[0 for _ in range(half*2-1)] for _ in range(half*2-1)]
        dd = "left"

        result = [] #[rStart, cStart]]
        for ii in range(0,rows*cols):

            while True:
                #print(dd, rStart, cStart, mr, mc)
                if dd == "up":
                    if matrix[mr][mc+1] == 0:
                        #matrix[mr][mc+1] = 1
                        cStart += 1
                        mc += 1
                        dd = "right"
                    else:
                        rStart -= 1
                        mr -= 1
                elif dd == "right":
                    if matrix[mr+1][mc] == 0:
                        #matrix[mr+1][mc] = 1
                        rStart += 1
                        mr += 1
                        dd = "down"
                    else:
                        cStart += 1
                        mc += 1
                elif dd == "down":
                    if matrix[mr][mc-1] == 0:
                        #matrix[mr][mc-1] = 1
                        cStart -= 1
                        mc -= 1
                        dd = "left"
                    else:
                        rStart += 1
                        mr += 1
                elif dd == "left":
                    #print(matrix[4][2])
                    if matrix[mr-1][mc] == 0:
                        #matrix[mr-1][mc] = 1
                        rStart -= 1
                        mr -= 1
                        dd = "up"
                    else:
                        cStart -= 1
                        mc -= 1
                matrix[mr][mc] = 1
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                    #print(rStart, cStart)
                    break

            result.append([rStart, cStart])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    print(app.leetcode(rows, cols, rStart, cStart))
