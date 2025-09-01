"""
207. Course Schedule
Solved
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
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
    def leetcode(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ll = len(prerequisites)
        dist = [-1]*numCourses
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
            #graph[b].append(a)

        self.loop = 0
        def dfs(start):
            if self.loop:
                return
            for c in graph[start]:
                if dist[c] == 0:
                    self.loop = 1
                elif dist[c] < 0:
                    dist[c] = dist[start]+1
                    dfs(c)

        for ii in range(numCourses):
            if self.loop:
                return False
            dist = [-1]*numCourses
            if dist[ii] == -1:
                dist[ii] = 0
                dfs(ii)

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
