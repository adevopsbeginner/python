"""
3459. Length of Longest V-Shaped Diagonal Segment
Attempted
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

 

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:



The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

 

Constraints:

n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
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
        m = len(grid)
        n = len(grid[0])

        for rr in range(m):
            for cc in range(n):
                grid[rr][cc] = [grid[rr][cc], 1,1,1,1]

        ### bottom left to top right
        for cc in range(1,n):
            for rr in range(m-2,-1,-1):
                if grid[rr][cc][0] == 1:
                    if grid[rr+1][cc-1][0] == 2:
                        grid[rr][cc][1] += grid[rr+1][cc-1][1]  
                elif grid[rr][cc][0] == 2:
                    if grid[rr+1][cc-1][0] == 0:
                        grid[rr][cc][1] += grid[rr+1][cc-1][1]
                elif grid[rr][cc][0] == 0:
                    if grid[rr+1][cc-1][0] == 2:
                        grid[rr][cc][1] += grid[rr+1][cc-1][1]

        ### top left to bottom right
        for rr in range(1,m):
            for cc in range(1,n):
                if grid[rr][cc][0] == 1:
                    if grid[rr-1][cc-1][0] == 2:
                        grid[rr][cc][2] += grid[rr-1][cc-1][2]
                elif grid[rr][cc][0] == 2:
                    if grid[rr-1][cc-1][0] == 0:
                        grid[rr][cc][2] += grid[rr-1][cc-1][2]
                elif grid[rr][cc][0] == 0:
                    if grid[rr-1][cc-1][0] == 2:
                        grid[rr][cc][2] += grid[rr-1][cc-1][2]

        ### bottom right to top left
        for cc in range(n-2,-1,-1):
            for rr in range(m-2,-1,-1):
                if grid[rr][cc][0] == 1:
                    if grid[rr+1][cc+1][0] == 2:
                        grid[rr][cc][3] += grid[rr+1][cc+1][3]
                elif grid[rr][cc][0] == 2:
                    if grid[rr+1][cc+1][0] == 0:
                        grid[rr][cc][3] += grid[rr+1][cc+1][3]
                elif grid[rr][cc][0] == 0:
                    if grid[rr+1][cc+1][0] == 2:
                        grid[rr][cc][3] += grid[rr+1][cc+1][3]

        ### top right to bottom left
        for cc in range(n-2,-1,-1):
            for rr in range(1,m):
                if grid[rr][cc][0] == 1:
                    if grid[rr-1][cc+1][0] == 2:
                        grid[rr][cc][4] += grid[rr-1][cc+1][4]
                elif grid[rr][cc][0] == 2:
                    if grid[rr-1][cc+1][0] == 0:
                        grid[rr][cc][4] += grid[rr-1][cc+1][4]
                elif grid[rr][cc][0] == 0:
                    if grid[rr-1][cc+1][0] == 2:
                        grid[rr][cc][4] += grid[rr-1][cc+1][4]

        # for rr in range(m):
        #     print(grid[rr])

        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc][0] == 0 or grid[rr][cc][0] == 2:
                    continue

                ### to bottom left turn top left     1-2
                for ii in range(1, max(m,n)):
                    next_r = rr+ii
                    if next_r >= m:
                        break
                    next_c = cc-ii
                    if next_c < 0:
                        break
                    if grid[next_r][next_c][0] == 1:
                        break
                    # if rr == 0 and cc == 5:
                    #     print(ii,rr, cc,grid[rr][cc][1], next_r, next_c, grid[next_r][next_c][2])
                    if ii == 1 and grid[next_r][next_c][0] == 0:
                        break
                    grid[rr][cc][1] = max(grid[rr][cc][1], ii+grid[next_r][next_c][2])

                    if grid[next_r][next_c][1] == 1:
                        break

                ### to top left turn top right       2-4
                for ii in range(1, max(m,n)):
                    next_r = rr-ii
                    if next_r < 0:
                        break
                    next_c = cc-ii
                    if next_c < 0:
                        break
                    if grid[next_r][next_c][0] == 1:
                        break
                    if ii == 1 and grid[next_r][next_c][0] == 0:
                        break
                    grid[rr][cc][2] = max(grid[rr][cc][2], ii+grid[next_r][next_c][4])

                    if grid[next_r][next_c][2] == 1:
                        break

                ### to bottom right turn bottom left 3-1
                for ii in range(1, max(m,n)):
                    next_r = rr+ii
                    if next_r >= m:
                        break
                    next_c = cc+ii
                    if next_c >= n:
                        break
                    if grid[next_r][next_c][0] == 1:
                        break
                    if ii == 1 and grid[next_r][next_c][0] == 0:
                        break
                    grid[rr][cc][3] = max(grid[rr][cc][3], ii+grid[next_r][next_c][1])

                    if grid[next_r][next_c][3] == 1:
                        break

                ### to top right turn  bottom right  4-3
                for ii in range(1, max(m,n)):
                    next_r = rr-ii
                    if next_r < 0:
                        break
                    next_c = cc+ii
                    if next_c >= n:
                        break
                    if grid[next_r][next_c][0] == 1:
                        break
                    if ii == 1 and grid[next_r][next_c][0] == 0:
                        break
                    # if rr == 2 and cc == 8:
                    #     print(ii,rr,cc,next_r, next_c, grid[next_r][next_c][3])
                    grid[rr][cc][4] = max(grid[rr][cc][4], ii+grid[next_r][next_c][3])

                    if grid[next_r][next_c][4] == 1:
                        break


        # for rr in range(m):
        #     print(grid[rr])
        
        result = 0
        for rr in range(m):
            for cc in range(n):
                if grid[rr][cc][0] == 1:
                    result = max(result, grid[rr][cc][1],grid[rr][cc][2],grid[rr][cc][3],grid[rr][cc][4])

        return result

        ### chatgpt
        
        n = len(grid)
        m = len(grid[0]) if n else 0
        if n == 0 or m == 0:
            return 0

        # Directions in clockwise order: SE, SW, NW, NE
        dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]
        dx = [d[0] for d in dirs]
        dy = [d[1] for d in dirs]
        def cw(d): return (d + 1) % 4

        # e -> value mapping: e=0 -> 0, e=1 -> 2, e=2 -> 1
        val_of_e = [0, 2, 1]
        # next expected mapping: 0->1, 1->0, 2->1
        next_e = [1, 0, 1]

        # dp[i][j][d][used][e]
        dp = [[[[[0]*3 for _ in range(2)] for _ in range(4)] for _ in range(m)] for _ in range(n)]

        def traversal_for_dir(d):
            # choose ranges so neighbor (i+dx[d], j+dy[d]) is computed first
            if d == 0:             # SE (1,1)
                i_range = range(n-1, -1, -1); j_range = range(m-1, -1, -1)
            elif d == 1:           # SW (1,-1)
                i_range = range(n-1, -1, -1); j_range = range(0, m, 1)
            elif d == 2:           # NW (-1,-1)
                i_range = range(0, n, 1);     j_range = range(0, m, 1)
            else:                  # NE (-1,1)
                i_range = range(0, n, 1);     j_range = range(m-1, -1, -1)
            return i_range, j_range

        # Phase 1: compute states with used = 1 (no further turn allowed)
        for d in range(4):
            i_range, j_range = traversal_for_dir(d)
            for i in i_range:
                for j in j_range:
                    for e in range(3):
                        if grid[i][j] != val_of_e[e]:
                            dp[i][j][d][1][e] = 0
                            continue
                        ne = next_e[e]
                        ni = i + dx[d]; nj = j + dy[d]
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == val_of_e[ne]:
                            dp[i][j][d][1][e] = 1 + dp[ni][nj][d][1][ne]
                        else:
                            dp[i][j][d][1][e] = 1

        # Phase 2: compute states with used = 0 (may take one clockwise turn)
        for d in range(4):
            i_range, j_range = traversal_for_dir(d)
            for i in i_range:
                for j in j_range:
                    for e in range(3):
                        if grid[i][j] != val_of_e[e]:
                            dp[i][j][d][0][e] = 0
                            continue
                        ne = next_e[e]

                        # straight candidate (depends on used=0 neighbor)
                        ni = i + dx[d]; nj = j + dy[d]
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == val_of_e[ne]:
                            straight = 1 + dp[ni][nj][d][0][ne]
                        else:
                            straight = 1

                        # turn candidate (uses used=1 at turned neighbor)
                        nd = cw(d)
                        ti = i + dx[nd]; tj = j + dy[nd]
                        turn = 0
                        if 0 <= ti < n and 0 <= tj < m and grid[ti][tj] == val_of_e[ne]:
                            turn = 1 + dp[ti][tj][nd][1][ne]

                        dp[i][j][d][0][e] = max(straight, turn)

        # answer: segments must start at value 1, with used=0 and e=2 (value 1)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, dp[i][j][d][0][2])
        return ans

        ### chatgpt, memroy limit exceeded
        n, m = len(grid), len(grid[0])
        dirs = [(1,1),(1,-1),(-1,1),(-1,-1)]  # ↘, ↙, ↗, ↖
        cw = {(1,1):(1,-1), (1,-1):(-1,-1), (-1,-1):(-1,1), (-1,1):(1,1)}

        def need(step):
            if step == 0: return 1
            return 2 if step % 2 else 0

        from functools import lru_cache

        #@lru_cache(None)
        def dfs(i, j, dx, dy, used, step):
            best = step + 1  # count current cell
            # straight
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and grid[x][y] == need(step + 1):
                best = max(best, dfs(x, y, dx, dy, used, step + 1))
            # optional single clockwise turn
            if not used:
                ndx, ndy = cw[(dx, dy)]
                x, y = i + ndx, j + ndy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == need(step + 1):
                    best = max(best, dfs(x, y, ndx, ndy, True, step + 1))
            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        ans = max(ans, dfs(i, j, dx, dy, False, 0))
        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
