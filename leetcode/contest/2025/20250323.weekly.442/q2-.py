"""
Q2. Properties Graph
Medium
4 pt.
You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph.

 

Example 1:

Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1

Output: 3

Explanation:

The graph formed has 3 connected components:



Example 2:

Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2

Output: 1

Explanation:

The graph formed has 1 connected component:



Example 3:

Input: properties = [[1,1],[1,1]], k = 2

Output: 2

Explanation:

intersect(properties[0], properties[1]) = 1, which is less than k. This means there is no edge between properties[0] and properties[1] in the graph.

 

Constraints:

1 <= n == properties.length <= 100
1 <= m == properties[i].length <= 100
1 <= properties[i][j] <= 100
1 <= k <= m
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, properties: List[List[int]], k: int) -> int:
        def intersect(a, b):
            seta = set(a)
            setb = set(b)
            setab = seta & setb
            return len(setab)

        def dfs(node):
            q = [node]
            while q:
                p = q.pop()
                if p not in visited:
                    visited.add(p)
                    for each in graph[p]:
                        q.append(each)

        n = len(properties)
        graph = defaultdict(list)
        for ii in range(n):
            for jj in range(ii+1,n):
                if intersect(properties[ii], properties[jj]) >= k:
                    graph[ii].append(jj)
                    graph[jj].append(ii)

        visited = set()
        result = 0
        for ii in range(n):
            if ii not in visited:
                dfs(ii)
                result += 1
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
