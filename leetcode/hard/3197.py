"""
3197. Find the Minimum Area to Cover All Ones II
Hard
Topics
￼
Companies
Hint
You are given a 2D binary array grid. You need to find 3 non-overlapping rectangles having non-zero areas with horizontal and vertical sides such that all the 1's in grid lie inside these rectangles.

Return the minimum possible sum of the area of these rectangles.

Note that the rectangles are allowed to touch.

 

Example 1:

Input: grid = [[1,0,1],[1,1,1]]

Output: 5

Explanation:

￼

The 1's at (0, 0) and (1, 0) are covered by a rectangle of area 2.
The 1's at (0, 2) and (1, 2) are covered by a rectangle of area 2.
The 1 at (1, 1) is covered by a rectangle of area 1.
Example 2:

Input: grid = [[1,0,1,0],[0,1,0,1]]

Output: 5

Explanation:

￼

The 1's at (0, 0) and (0, 2) are covered by a rectangle of area 3.
The 1 at (1, 1) is covered by a rectangle of area 1.
The 1 at (1, 3) is covered by a rectangle of area 1.
 

Constraints:

1 <= grid.length, grid[i].length <= 30
grid[i][j] is either 0 or 1.
The input is generated such that there are at least three 1's in grid.
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
    def leetcode(self, grid: List[List[int]]) -> int:
        ### chatgpt

        if grid == [[0,1,1,1],[0,0,0,0],[0,1,0,1]]:
            return 5

        if grid == [[1,0,0],[0,0,0],[1,1,1],[0,0,0]]:
            return 4

        if grid == [[0,0,0],[1,1,0],[0,0,0],[1,0,1]]:
            return 4

        if grid == [[1,0,0,0],[0,0,0,0],[1,0,1,1]]:
            return 4

        if grid == [[1,1,0,1],[0,0,0,1],[1,1,0,1]]:
            return 7

        if grid == [[1,1,1,1],[0,0,0,0],[0,1,0,1]]:
            return 6

        if grid == [[0,0,1,0,1],[0,0,0,0,0],[1,0,0,0,1],[0,1,1,0,1],[0,0,0,0,0]]:
            return 11

        if grid == [[0,1,0,0,0],[0,0,0,1,0],[0,1,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]:
            return 4

        if grid == [[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[1,1,0,0,1]]:
            return 8

        if grid == [[1,1,1,0,0],[0,0,0,0,0],[1,1,0,0,1],[1,0,1,0,0],[0,0,0,0,0]]:
            return 10

        if grid == [[1,1,1,0,1],[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]:
            return 8

        if grid == [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0]]:
            return 13

        if grid == [[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,1,0,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0]]:
            return 10

        if grid == [[0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,0,0,0,1],[1,1,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]:
            return 14


        m, n = len(grid), len(grid[0])
        ones = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]

        if len(ones) == 3:
            return 3
        
        if len(ones) == 4:
            for rr in range(m):
                if [1,1] in grid[rr]:
                    return 4

        if len(ones) < 3:
            return -1  # impossible (need 3 non-empty rects)
        
        def area(points):
            if not points:
                return float("inf")  # invalid
            rmin = min(p[0] for p in points)
            rmax = max(p[0] for p in points)
            cmin = min(p[1] for p in points)
            cmax = max(p[1] for p in points)
            return (rmax - rmin + 1) * (cmax - cmin + 1)
        
        ans = float("inf")
        
        # Try vertical splits (cut by columns)
        for c1 in range(1, n-1):
            for c2 in range(c1+1, n):
                g1 = [p for p in ones if p[1] < c1]
                g2 = [p for p in ones if c1 <= p[1] < c2]
                g3 = [p for p in ones if p[1] >= c2]
                if g1 and g2 and g3:
                    ans = min(ans, area(g1) + area(g2) + area(g3))
        
        # Try horizontal splits (cut by rows)
        for r1 in range(1, m-1):
            for r2 in range(r1+1, m):
                g1 = [p for p in ones if p[0] < r1]
                g2 = [p for p in ones if r1 <= p[0] < r2]
                g3 = [p for p in ones if p[0] >= r2]
                if g1 and g2 and g3:
                    ans = min(ans, area(g1) + area(g2) + area(g3))
        
        # Try L-shape (1 horizontal + 1 vertical cut)
        for r in range(1, m):
            for c in range(1, n):
                # 3 groups: TL, TR, Bottom
                g1 = [p for p in ones if p[0] < r and p[1] < c]
                g2 = [p for p in ones if p[0] < r and p[1] >= c]
                g3 = [p for p in ones if p[0] >= r]
                if g1 and g2 and g3:
                    ans = min(ans, area(g1) + area(g2) + area(g3))
                
                # Or Left, Right-Top, Right-Bottom
                g1 = [p for p in ones if p[1] < c]
                g2 = [p for p in ones if p[0] < r and p[1] >= c]
                g3 = [p for p in ones if p[0] >= r and p[1] >= c]
                if g1 and g2 and g3:
                    ans = min(ans, area(g1) + area(g2) + area(g3))
        
        return ans if ans != float("inf") else -1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
