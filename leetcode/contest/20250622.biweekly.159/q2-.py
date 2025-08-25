"""
Q2. Find Maximum Area of a Triangle
Medium
4 pt.
You are given a 2D array coords of size n x 2, representing the coordinates of n points in an infinite Cartesian plane.

Find twice the maximum area of a triangle with its corners at any three elements from coords, such that at least one side of this triangle is parallel to the x-axis or y-axis. Formally, if the maximum area of such a triangle is A, return 2 * A.

If no such triangle exists, return -1.

Note that a triangle cannot have zero area.

 

Example 1:

Input: coords = [[1,1],[1,2],[3,2],[3,3]]

Output: 2

Explanation:



The triangle shown in the image has a base 1 and height 2. Hence its area is 1/2 * base * height = 1.

Example 2:

Input: coords = [[1,1],[2,2],[3,3]]

Output: -1

Explanation:

The only possible triangle has corners (1, 1), (2, 2), and (3, 3). None of its sides are parallel to the x-axis or the y-axis.

 

Constraints:

1 <= n == coords.length <= 105
1 <= coords[i][0], coords[i][1] <= 106
All coords[i] are unique.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, coords: List[List[int]]) -> int:
        xmax = ymax = 0
        xmin = ymin = 100000001
        ddxmax = defaultdict(int)
        ddxmin = defaultdict(int)
        ddymax = defaultdict(int)
        ddymin = defaultdict(int)
        ll = len(coords)

        result = -1
        for ii in range(ll):
            x,y = coords[ii]
            xmax = max(xmax, x)
            xmin = min(xmin, x)
            ymax = max(ymax, y)
            ymin = min(ymin, y)

            if x in ddxmax:
                ddxmax[x] = max(ddxmax[x], y)
                ddxmin[x] = min(ddxmin[x], y)
            else:
                ddxmax[x] = y
                ddxmin[x] = y

            if y in ddymax:
                ddymax[y] = max(ddymax[y], x)
                ddymin[y] = min(ddymin[y], x)
            else:
                ddymax[y] = x
                ddymin[y] = x

        # print(xmax, xmin)
        # print(ymax, ymin)
        # print(ddxmax)
        # print(ddxmin)
        # print(ddymax)
        # print(ddymin)

        for ii in range(ll):
            x, y = coords[ii]
            if ddxmax[x] == ddxmin[x]:
                continue
            #print("xxx", x, y, result)
            if x != xmax:
                result = max(result, (ddxmax[x] - ddxmin[x])*(xmax-x))
            if x != xmin:
                result = max(result, (ddxmax[x] - ddxmin[x])*(x-xmin))

        for ii in range(ll):
            x, y = coords[ii]
            if ddymax[y] == ddymin[y]:
                continue
            #print("yyy", x, y, result)
            if y != ymax:
                result = max(result, (ddymax[y] - ddymin[y])*(ymax-y))
            if y != ymin:
                result = max(result, (ddymax[y] - ddymin[y])*(y-ymin))
            
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
