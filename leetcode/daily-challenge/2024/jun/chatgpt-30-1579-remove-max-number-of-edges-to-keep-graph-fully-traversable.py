"""
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard
Topics
Companies
Hint
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.



Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.




Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
"""

import string
import heapq
from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n  # Number of connected components

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            self.count -= 1
            return True
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Initialize Union-Find structures for Alice and Bob
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        # Number of edges used in the final solution
        edges_used = 0

        # First, handle all type 3 edges (both Alice and Bob can use these)
        for edge in edges:
            if edge[0] == 3:
                if uf_alice.union(edge[1] - 1, edge[2] - 1):
                    uf_bob.union(edge[1] - 1, edge[2] - 1)
                    edges_used += 1

        # Handle type 1 edges (only Alice can use these)
        for edge in edges:
            if edge[0] == 1:
                if uf_alice.union(edge[1] - 1, edge[2] - 1):
                    edges_used += 1

        # Handle type 2 edges (only Bob can use these)
        for edge in edges:
            if edge[0] == 2:
                if uf_bob.union(edge[1] - 1, edge[2] - 1):
                    edges_used += 1

        # Check if both Alice and Bob can traverse the entire graph
        if uf_alice.count > 1 or uf_bob.count > 1:
            return -1

        # The maximum number of edges we can remove is total edges minus the edges used
        return len(edges) - edges_used


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    a = [0,2,2]
    #a = [3,2,1,2,1,7]
    b = [5]
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    print(app.leetcode(k,w,profits,capital))
