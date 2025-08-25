"""
399. Evaluate Division
Solved
Medium
Topics
￼
Companies
Hint
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
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
    def leetcode(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        flate = [item for sublist in equations for item in sublist]
        flate = list(set(flate))
        #print(flate)
        lf = len(flate)
        mtx = [[0 for ii in range(lf)] for jj in range(lf)]
        le = len(equations)
        graph = defaultdict(list)
        for ii in range(le):
            a = equations[ii][0]
            b = equations[ii][1]
            ia = flate.index(a)
            ib = flate.index(b)
            mtx[ia][ib] = values[ii]
            mtx[ib][ia] = 1/values[ii]
            graph[a].append(b)
            graph[b].append(a)
            
        def product(c):
            ans = 1
            lc = len(c)
            for ii in range(1,lc):
                ans *= mtx[flate.index(c[ii-1])][flate.index(c[ii])]
                
            return ans
            
        def dfs(da,db):
            q = [[da]]
            while len(q):
                c = q.pop()
                if c[-1] == db:
                    return product(c)
                for each in graph[c[-1]]:
                    if each not in c:
                        q.append(c+[each])
            return -1
            
        ans = []
        #print(mtx)
        for qa,qb in queries:
            #print(qa,qb)
            if qa not in flate or qb not in flate:
                ans.append(-1)
                continue
            if qa == qb:
                ans.append(1)
                continue
            qv = dfs(qa,qb)
            ans.append(qv)

        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
