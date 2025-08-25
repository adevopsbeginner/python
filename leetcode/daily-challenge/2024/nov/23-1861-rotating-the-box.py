"""
1861. Rotating the Box
Medium
Topics
Companies
Hint
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
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
    def leetcode(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])

        for r in range(m):
            count0 = 0
            count1 = 0
            for c in range(n):
                if box[r][c] == "#":
                    count1 += 1
                elif box[r][c] == ".":
                    count0 += 1
                else:
                    if count1 == 0:
                        count0 = 0
                        continue
                    for ii in range(c-(count0+count1), c-count1):
                        box[r][ii] = "."
                    for ii in range(c-count1,c):
                        box[r][ii] = "#"
                    count0 = 0
                    count1 = 0

                if count1 > 0 and c == n-1:
                    for ii in range(n-(count0+count1), n-count1):
                        box[r][ii] = "."
                    for ii in range(n-count1,n):
                        box[r][ii] = "#"

        result = [[box[m-1-r][c] for r in range(m)] for c in range(n)]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
