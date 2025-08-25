"""
Q1. Count Covered Buildings
Medium
4 pt.
You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

 

Example 1:



Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

Output: 1

Explanation:

Only building [2,2] is covered as it has at least one building:
above ([1,2])
below ([3,2])
left ([2,1])
right ([2,3])
Thus, the count of covered buildings is 1.
Example 2:



Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

Output: 0

Explanation:

No building has at least one building in all four directions.
Example 3:



Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

Output: 1

Explanation:

Only building [3,3] is covered as it has at least one building:
above ([1,3])
below ([5,3])
left ([3,2])
right ([3,5])
Thus, the count of covered buildings is 1.
 

Constraints:

2 <= n <= 105
1 <= buildings.length <= 105 
buildings[i] = [x, y]
1 <= x, y <= n
All coordinates of buildings are unique.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int, buildings: List[List[int]]) -> int:
        x_left = [100000]*(n+1)
        x_right = [0]*(n+1)
        y_left = [100000]*(n+1)
        y_right = [0]*(n+1)
        ll = len(buildings)
        for x,y in buildings:
            x_left[y] = min(x_left[y], x)
            x_right[y] = max(x_right[y], x)
            y_left[x] = min(y_left[x], y)
            y_right[x] = max(y_right[x], y)
        # print(x_left)
        # print(x_right)
        # print(y_left)
        # print(y_right)
        result = ll
        for x,y in buildings:
            if x > x_left[y] and x < x_right[y] and y > y_left[x] and y < y_right[x]:
                #print(x,y)
                continue
            result -= 1
                
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
