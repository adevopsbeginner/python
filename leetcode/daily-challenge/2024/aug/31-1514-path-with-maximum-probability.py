"""

Code
Testcase
Test Result
Test Result
1514. Path with Maximum Probability
Solved
Medium
Topics
Companies
Hint
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.



Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.


Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
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
    def leetcode(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        start = start_node
        end = end_node
        # Step 1: Build the graph as an adjacency list
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        # Step 2: Max-heap priority queue with initial probability of 1 for the start node
        max_heap = [(-1.0, start)]  # (-probability, node)
        max_prob = [0.0] * n  # To store the maximum probability to reach each node
        max_prob[start] = 1.0

        # Step 3: Perform a modified Dijkstra's algorithm
        while max_heap:
            # Pop the node with the highest probability
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob  # Convert back to positive

            # If we reached the end node, return the current probability
            if node == end:
                return curr_prob

            # Visit all neighbors
            for neighbor, edge_prob in graph[node]:
                # Calculate the new probability via this edge
                new_prob = curr_prob * edge_prob
                # If this path gives a higher probability, update and push to the heap
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        # If the end node is unreachable, return 0
        return 0.0

        def dfs(start: int):
            if start == end_node:
                return 1

            for each in graph[start]:
                if each in been:
                    continue
                been.append(each)
                matrix[start][end_node] = max(matrix[start][end_node], matrix[start][each]*dfs(each))
            return matrix[start][end_node]

        result = 0
        # graph = defaultdict(list)
        matrix = [[0.0 for _ in range(n)] for _ in range(n)]
        for ii in range(n):
            matrix[ii][ii] = 1
        for ii in range(len(edges)):
            matrix[edges[ii][0]][edges[ii][1]] = succProb[ii]
            matrix[edges[ii][1]][edges[ii][0]] = succProb[ii]
            # graph[edges[ii][0]].append(edges[ii][1])
            # graph[edges[ii][1]].append(edges[ii][0])
        for ii in range(n-1):
            for jj in range(ii+1,n):
                for kk in range(n):
                    matrix[ii][jj] = max(matrix[ii][jj], matrix[ii][kk] * matrix[kk][jj])
                    matrix[jj][ii] = matrix[ii][jj]
        return matrix[start_node][end_node]

        # been = [start_node]
        # result = dfs(start_node)
        # # print(matrix)

        # return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
