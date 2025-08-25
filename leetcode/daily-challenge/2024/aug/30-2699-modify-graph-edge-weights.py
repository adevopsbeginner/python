"""
2699. Modify Graph Edge Weights
Hard
Topics
Companies
Hint
You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.



Example 1:



Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
Example 2:



Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
Example 3:



Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.


Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges
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
    def leetcode(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        ### chatgpt, but wrong answer
        def dijkstra(n, graph, source):
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]

            while pq:
                d, node = heapq.heappop(pq)

                if d > dist[node]:
                    continue

                for nei, weight in graph[node]:
                    new_dist = d + weight
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(pq, (new_dist, nei))

            return dist

    #def modify_and_find_path(n, edges, source, destination, target):
        graph = defaultdict(list)

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        initial_dist = dijkstra(n, graph, source)

        if initial_dist[destination] < target:
            return []

        if initial_dist[destination] == target:
            return edges

        for i in range(len(edges)):
            if edges[i][2] == -1:
                edges[i][2] = 1

        low, high = 1, 2 * 10**9

        while low <= high:
            mid = (low + high) // 2

            for i in range(len(edges)):
                if edges[i][2] == 1:
                    edges[i][2] = mid

            graph = defaultdict(list)

            for u, v, w in edges:
                graph[u].append((v, w))
                graph[v].append((u, w))

            dist = dijkstra(n, graph, source)

            if dist[destination] == target:
                return edges
            elif dist[destination] < target:
                low = mid + 1
            else:
                high = mid - 1

        return []

        def dijkstra(n, adj, source):
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, weight in adj[node]:
                    if dist[nei] > d + weight:
                        dist[nei] = d + weight
                        heapq.heappush(pq, (dist[nei], nei))
            return dist
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))

        # Compute the shortest path using only positive edges
        original_dist = dijkstra(n, adj, source)

        # If the shortest distance already exceeds the target, return empty
        if original_dist[destination] < target:
            # Try to minimize all -1 edges
            for i, (u, v, w) in enumerate(edges):
                if w == -1:
                    edges[i][2] = 1
                    adj[u].append((v, 1))
                    adj[v].append((u, 1))
            new_dist = dijkstra(n, adj, source)

            if new_dist[destination] == target:
                return edges
            elif new_dist[destination] < target:
                diff = target - new_dist[destination]
                for i, (u, v, w) in enumerate(edges):
                    if w == 1:
                        edges[i][2] += diff
                        break
                return edges
        return []
    #def modify_graph_to_meet_target(n, edges, source, destination, target):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if w != -1:
                adj[u].append((v, w))
                adj[v].append((u, w))

        original_dist = dijkstra(n, adj, source)
        if original_dist[destination] < target:
            for i, (u, v, w) in enumerate(edges):
                if w == -1:
                    edges[i][2] = 1
                    adj[u].append((v, 1))
                    adj[v].append((u, 1))
            new_dist = dijkstra(n, adj, source)
            if new_dist[destination] == target:
                return edges
            elif new_dist[destination] < target:
                diff = target - new_dist[destination]
                for i, (u, v, w) in enumerate(edges):
                    if w == 1:
                        edges[i][2] += diff
                        break
                return edges
        return []


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
