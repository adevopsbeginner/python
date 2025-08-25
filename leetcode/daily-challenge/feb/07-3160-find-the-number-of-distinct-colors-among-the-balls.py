"""
3160. Find the Number of Distinct Colors Among the Balls
Medium
Topics
Companies
Hint
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

 

Example 1:

Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]

Output: [1,2,2,3]

Explanation:



After query 0, ball 1 has color 4.
After query 1, ball 1 has color 4, and ball 2 has color 5.
After query 2, ball 1 has color 3, and ball 2 has color 5.
After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.
Example 2:

Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]

Output: [1,2,2,3,4]

Explanation:



After query 0, ball 0 has color 1.
After query 1, ball 0 has color 1, and ball 1 has color 2.
After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.
After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.
 

Constraints:

1 <= limit <= 109
1 <= n == queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= limit
1 <= queries[i][1] <= 109
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
    def leetcode(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = [0]*n
        dcolor = {}
        dball = {}
        count = 0
        for ii in range(n):
            ball,color = queries[ii]
            if ball in dball:
                dcolor[dball[ball]].remove(ball)
                if len(dcolor[dball[ball]]) == 0:
                    count -= 1
                dball[ball] = color
            else:
                dball[ball] = color
            
            if color in dcolor: ## existing color
                llc = len(dcolor[color])
                if llc == 0: ### "new color"
                    dcolor[color] = [ball]
                    count += 1
                else:
                    if ball not in dcolor[color]:
                        dcolor[color].append(ball)
            else: ## new color
                dcolor[color] = [ball]
                count += 1

            result[ii] = count

        ### memory limit exceeded
        # #balls = [0]*(limit+1)
        # for ii in range(n):
        #     ball,color = queries[ii]
        #     if balls[ball] > 0:
        #         dd[balls[ball]] -= 1
        #     balls[ball] = color
        #     dd[color] += 1

        #     count = 0
        #     for each in dd:
        #         if dd[each] > 0:
        #             count += 1
        #     result[ii] = count

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
