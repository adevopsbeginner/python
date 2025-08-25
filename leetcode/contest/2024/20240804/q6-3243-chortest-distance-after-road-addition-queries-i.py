"""
3243. Shortest Distance After Road Addition Queries I
Attempted
Medium
Companies
Hint
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.



Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:



After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:



After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.



After the addition of the road from 0 to 2, the length of the shortest path remains 1.



Constraints:

3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
There are no repeated roads among the queries.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int, queries: List[List[int]]) -> List[int]:
        ### time exceeded
        short = n-1
        grid = [[jj-ii for jj in range(n)] for ii in range(n)]
        ll = len(queries)
        result = [0] * ll
        a = n-1
        b = 0

        for kk in range(ll):
            u,v = queries[kk]
            flag = 0
            for pp in range(kk):
                u1,v1 = queries[pp]
                if u1 >= u and v1 <= v:
                    flag = 1
                    break
            if flag:
                continue

            if grid[0][n-1] == 1:
                pass
            elif u == 0 and v == n-1:
                grid[0][n-1] = 1
            else:
                #short = min(short,grid[0][u]+1+grid[v][n-1])
                for ii in range(u+1):
                    for jj in range(max(ii,v),n):
                        #if ii <= jj and u >= ii and v<=jj:
                        grid[ii][jj] = min(grid[ii][jj],grid[ii][u]+1+grid[v][jj])
            result[kk] = grid[0][n-1]

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
