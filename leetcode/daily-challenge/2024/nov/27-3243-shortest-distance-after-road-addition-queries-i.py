"""
3243. Shortest Distance After Road Addition Queries I
Solved
Medium
Topics
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
    def leetcode(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize graph
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        # BFS function to find the shortest path
        def bfs():
            dist = [-1] * n
            dist[0] = 0
            queue = deque([0])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if dist[neighbor] == -1:  # Not visited
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
            return dist[n - 1]  # Distance to the last city
        
        # Process each query and compute the shortest path
        answer = []
        for u, v in queries:
            graph[u].append(v)
            answer.append(bfs())
        
        return answer
        ll = len(queries)
        matrix = [[c-r for c in range(n)] for r in range(n)]
        result = [1] * (ll)

        for ii in range(ll):
            if matrix[0][n-1] == 1:
                break
            a,b = queries[ii]
            matrix[a][b] = 1
            for aa in range(a+1):
                for bb in range(b,n):
                    matrix[aa][bb] = min(matrix[aa][bb], matrix[aa][a]+1+matrix[b][bb])
            result[ii] = matrix[0][n-1]
            #print(matrix)

        return result
   


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
