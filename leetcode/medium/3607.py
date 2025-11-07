"""
3607. Power Grid Maintenance
Attempted
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:



Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

There are no connections, so each station is its own isolated grid.
Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
Query [2,1]: Station 1 goes offline.
Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
 

Constraints:

1 <= c <= 105
0 <= n == connections.length <= min(105, c * (c - 1) / 2)
connections[i].length == 2
1 <= ui, vi <= c
ui != vi
1 <= queries.length <= 2 * 105
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
"""

import string
import heapq
from typing import List
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class PowerGrid:
    def __init__(self, n, connections):
        self.n = n
        self.dsu = DSU(n)
        
        # Build DSU
        for a, b in connections:
            self.dsu.union(a, b)
        
        # Collect nodes by component
        self.comp_nodes = {}
        for i in range(1, n + 1):
            root = self.dsu.find(i)
            if root not in self.comp_nodes:
                self.comp_nodes[root] = set()
            self.comp_nodes[root].add(i)
        
        # Each component keeps a sorted list of online stations
        from bisect import insort
        self.online = [True] * (n + 1)
        self.comp_online = {root: sorted(nodes) for root, nodes in self.comp_nodes.items()}

    def take_offline(self, x):
        if not self.online[x]:
            return
        self.online[x] = False
        root = self.dsu.find(x)
        arr = self.comp_online[root]
        # Remove x from sorted list (binary search)
        import bisect
        i = bisect.bisect_left(arr, x)
        if i < len(arr) and arr[i] == x:
            arr.pop(i)

    def check(self, x):
        if self.online[x]:
            return x
        root = self.dsu.find(x)
        arr = self.comp_online[root]
        if not arr:
            return -1
        return arr[0]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)

        # 1️⃣ Build DSU from connections
        for a, b in connections:
            dsu.union(a, b)

        # 2️⃣ Group stations by component
        comp_nodes = {}
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp_nodes.setdefault(root, []).append(i)

        # 3️⃣ Maintain a sorted list of online stations per component
        comp_online = {root: sorted(nodes) for root, nodes in comp_nodes.items()}
        online = [True] * (c + 1)

        res = []

        # 4️⃣ Process queries
        for t, x in queries:
            if t == 1:  # Check query
                if online[x]:
                    res.append(x)
                else:
                    root = dsu.find(x)
                    arr = comp_online[root]
                    res.append(arr[0] if arr else -1)
            else:  # t == 2 → Take offline
                if online[x]:
                    online[x] = False
                    root = dsu.find(x)
                    arr = comp_online[root]
                    i = bisect.bisect_left(arr, x)
                    if i < len(arr) and arr[i] == x:
                        arr.pop(i)

        return res
        
        def dfs(node, visited, same_grid, depth):
            depth += 1
            for each in graph[node]:
                #print(node, each, visited, same_grid, graph[each], depth)
                if visited[each] == 1:
                    continue
                visited[node] = 1
                if each not in same_grid:
                    same_grid.append(each)
                same_grid = dfs(each, visited, same_grid, depth)
            return same_grid
            
        online = [1]*(c+1)
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        result = []
        same_grid = [None] * (c+1)
        for check,station in queries:
            if check == 2:
                online[station] = 0
            elif check == 1:
                if online[station] == 1:
                    result.append(station)
                elif online[station] == 0:
                    if same_grid[station] == None:
                        same_grid[station] = [station] + graph[station]
                        visited = [0]*(c+1)
                        visited[station] = 1
                        same_grid[station] = dfs(station, visited, same_grid[station], 0)
                        for each in same_grid[station]:
                            same_grid[each] = same_grid[station]
                        #print(check, station, same_grid[station])
                        same_grid[station].sort()
                    result.append(-1)
                    for each in same_grid[station]:
                        if online[each] == 1:
                            result[-1] = each
                            break

        return result
