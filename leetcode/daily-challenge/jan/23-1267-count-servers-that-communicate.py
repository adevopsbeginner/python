"""
1267. Count Servers that Communicate
Medium
Topics
Companies
Hint
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
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
    def leetcode(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        
        ### init sum of each row/column
        sum_r = [0]*m
        sum_c = [0]*n

        ### calculate sum of each row/column
        for ii in range(m):
            for jj in range(n):
                sum_r[ii] += grid[ii][jj]
                sum_c[jj] += grid[ii][jj]

        for ii in range(m):
            ### no node
            if sum_r[ii] == 0:
                continue
            ### multiple nodes
            elif sum_r[ii] > 1:
                result += sum_r[ii]
            ### single node in the row
            elif sum_r[ii] == 1:
                for jj in range(n):
                    if grid[ii][jj] == 1:
                        ### but multiple nodes in the column
                        if sum_c[jj] > 1:
                            result += 1
                        break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
