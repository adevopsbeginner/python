"""
Q4. Time Taken to Mark All Nodes
Hard
7 pt.
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.

Initially, all nodes are unmarked. For each node i:

If i is odd, the node will get marked at time x if there is at least one node adjacent to it which was marked at time x - 1.
If i is even, the node will get marked at time x if there is at least one node adjacent to it which was marked at time x - 2.
Return an array times where times[i] is the time when all nodes get marked in the tree, if you mark node i at time t = 0.

Note that the answer for each times[i] is independent, i.e. when you mark node i all other nodes are unmarked.



Example 1:

Input: edges = [[0,1],[0,2]]

Output: [2,4,3]

Explanation:



For i = 0:
Node 1 is marked at t = 1, and Node 2 at t = 2.
For i = 1:
Node 0 is marked at t = 2, and Node 2 at t = 4.
For i = 2:
Node 0 is marked at t = 2, and Node 1 at t = 3.
Example 2:

Input: edges = [[0,1]]

Output: [1,2]

Explanation:



For i = 0:
Node 1 is marked at t = 1.
For i = 1:
Node 0 is marked at t = 2.
Example 3:

Input: edges = [[2,4],[0,1],[2,3],[0,2]]

Output: [4,6,3,5,5]

Explanation:





Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
The input is generated such that edges represents a valid tree.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, edges: List[List[int]]) -> List[int]:
        ### time exceeded
        def dfs(node: int) -> int:
            maxtime = 0
            for each in graph[node]:
                if flag[each]:
                    continue
                flag[each] = 1
                if each & 1:
                    maxtime = max(maxtime,1+dfs(each))
                else:
                    maxtime = max(maxtime,2+dfs(each))

            return maxtime

        n = len(edges)+1
        result = [0] * n
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for ii in range(n):
            flag = [0] * n
            flag[ii] = 1
            result[ii] = dfs(ii)

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
