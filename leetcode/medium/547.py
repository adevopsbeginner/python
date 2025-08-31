"""
547. Number of Provinces
Medium
Topics
premium lock icon
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
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
    def leetcode(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited[start] =1
            for each in graph[start]:
                if visited[each] == 0:
                    dfs(each)
        
        n = len(isConnected)
        graph = defaultdict(list)
        for rr in range(n):
            for cc in range(n):
                if isConnected[rr][cc]:
                    graph[rr].append(cc)
                    graph[cc].append(rr)

        visited = [0]*n
        result = 0
        for ii in range(n):
            if visited[ii] == 0:
                result += 1
                dfs(ii)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
