"""
733. Flood Fill
Solved
Easy
Topics
Companies
Hint
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.



Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
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
    def leetcode(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def bfs(r: int, c: int):
            if c > 0 and image[r][c-1] == save and matrix[r][c-1] == 0:
                image[r][c-1] = color
                matrix[r][c-1] = 1
                bfs(r,c-1)
            if c < n-1 and image[r][c+1] == save and matrix[r][c+1] == 0:
                image[r][c+1] = color
                matrix[r][c+1] = 1
                bfs(r,c+1)
            if r > 0 and image[r-1][c] == save and matrix[r-1][c] == 0:
                image[r-1][c] = color
                matrix[r-1][c] = 1
                bfs(r-1,c)
            if r < m-1 and image[r+1][c] == save and matrix[r+1][c] == 0:
                image[r+1][c] = color
                matrix[r+1][c] = 1
                bfs(r+1,c)

        m = len(image)
        n = len(image[0])
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        save = image[sr][sc]
        matrix[sr][sc] = 1
        image[sr][sc] = color
        bfs(sr,sc)

        return image



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
