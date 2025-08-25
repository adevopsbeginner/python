"""
1791. Find Center of Star Graph
Solved
Easy
Topics
Companies
Hint
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.



Example 1:


Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1


Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
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
    def leetcode(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    ancestors[neighbor].update(ancestors[node])
                    ancestors[neighbor].add(node)
                    visited[neighbor] = 1
                    dfs(neighbor)

        graph = defaultdict(list)
        for frm, to in edges:
            graph[frm].append(to)

        ancestors = [set() for _ in range(n)]

        for node in range(n):
            visited = [0 for _ in range(n)]
            visited[node] = 1
            dfs(node)

        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]

        ### no
        result = [[] for ii in range(n)]
        parent = [[] for ii in range(n)]
        for each in edges:
            # print(result)
            parent[each[0]].append(each[1])
            result[each[1]].append(each[0])
        return result

if __name__ == "__main__":
    app = Solution()
    a = 8
    b = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
    a = 9
    b = [[3,6],[2,4],[8,6],[7,4],[1,4],[2,1],[7,2],[0,4],[5,0],[4,6],[3,2],[5,6],[1,6]]

    print(app.leetcode(a,b))
