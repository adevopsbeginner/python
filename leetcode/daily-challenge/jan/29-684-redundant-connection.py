"""


684. Redundant Connection
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
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
    def leetcode(self, edges: List[List[int]]) -> List[int]:
        def dfs(a: int, parent: int) -> bool:
            visited[a] = 1
            for each in graph[a]:
                if visited[each] == 1:
                    if each != parent:
                        return False
                else:
                    if not dfs(each, a):
                        return False
            return True

        graph = defaultdict(list)
        ll = len(edges)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for ii in range(ll-1,-1,-1):
            visited = [0]*(ll+1)
            a,b = edges[ii][0], edges[ii][1]
            if len(graph[a]) < 2:
                continue
            if len(graph[b]) < 2:
                continue
            graph[a].remove(b)
            graph[b].remove(a)
            # if dfs(a, -1):
            #     print(a,b, 111)
            # if dfs(b, -1):
            #     print(a, b,222)
            if dfs(a, -1):
                visited = [0]*(ll+1)
                if dfs(b, -1):
                    return [a,b]
            graph[a].append(b)
            graph[b].append(a)

        return edges[0]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
