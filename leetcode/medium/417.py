"""
417. Pacific Atlantic Water Flow
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
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
    def leetcode(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(rr, cc):
            if rr > 0:
                if heights[rr-1][cc] < heights[rr][cc]:
                    pass
                elif labels[rr-1][cc] == 3:
                    pass
                elif labels[rr-1][cc] == labels[rr][cc]:
                    pass
                else:
                    labels[rr-1][cc] |= labels[rr][cc]
                    dfs(rr-1, cc)

            if rr < m-1:
                if heights[rr+1][cc] < heights[rr][cc]:
                    pass
                elif labels[rr+1][cc] == 3:
                    pass
                elif labels[rr+1][cc] == labels[rr][cc]:
                    pass
                else:
                    labels[rr+1][cc] |= labels[rr][cc]
                    dfs(rr+1, cc)

            if cc > 0:
                if heights[rr][cc-1] < heights[rr][cc]:
                    pass
                elif labels[rr][cc-1] == 3:
                    pass
                elif labels[rr][cc-1] == labels[rr][cc]:
                    pass
                else:
                    labels[rr][cc-1] |= labels[rr][cc]
                    dfs(rr, cc-1)

            if cc < n-1:
                if heights[rr][cc+1] < heights[rr][cc]:
                    pass
                elif labels[rr][cc+1] == 3:
                    pass
                elif labels[rr][cc+1] == labels[rr][cc]:
                    pass
                else:
                    labels[rr][cc+1] |= labels[rr][cc]
                    dfs(rr, cc+1)

        m = len(heights)
        n = len(heights[0])

        ### step 1, labels
        labels = [[0]*n for _ in range(m)]

        for rr in range(m):
            labels[rr][0] |= 1
            labels[rr][n-1] |= 2

        for cc in range(n):
            labels[0][cc] |= 1
            labels[m-1][cc] |= 2

        #labels[0][n-1] = 3
        #labels[m-1][0] = 3

        ### step 2, dfs
        for rr in range(m):
            for cc in range(n):
                dfs(rr,cc)

        #print(labels)
        
        result = []
        for rr in range(m):
            for cc in range(n):
                if labels[rr][cc] == 3:
                    result.append([rr,cc])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
