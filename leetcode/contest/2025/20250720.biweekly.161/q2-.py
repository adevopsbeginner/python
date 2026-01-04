"""
Q2. Count Islands With Total Value Divisible by K
Medium
4 pt.
You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

 

Example 1:


Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:


Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
0 <= grid[i][j] <= 106
1 <= k <= 106©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, grid: List[List[int]], k: int) -> int:
        def label(rr, cc, island_no):
            if grid[rr][cc] == 0:
                return
                
            if visited[rr][cc] > 0:
                return
                
            visited[rr][cc] = island_no
            if rr > 0:
                label(rr-1, cc, island_no)
            if rr < m-1:
                label(rr+1, cc, island_no)
            if cc > 0:
                label(rr, cc-1, island_no)
            if cc < n-1:
                label(rr, cc+1, island_no)

        m = len(grid)
        n = len(grid[0])
        island_no = 1
        visited = [[0 for _ in range(n)] for _ in range(m)]

        ### step1 labelling islands
        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc] == 0:
                    continue
                if visited[rr][cc] == 0:
                    label(rr,cc, island_no)
                    island_no += 1

        ### step2 sum total values
        total_values = defaultdict(int)
        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc] > 0:
                    total_values[visited[rr][cc]] += grid[rr][cc]

        ### step3 count result
        result = 0
        for each in total_values:
            if total_values[each]%k == 0:
                result += 1
                
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
