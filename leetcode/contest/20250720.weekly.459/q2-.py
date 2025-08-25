"""
Q2. Count Number of Trapezoids I
Medium
4 pt.
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:



There are three distinct ways to pick four points that form a horizontal trapezoid:

Using points [1,0], [2,0], [3,2], and [2,2].
Using points [2,0], [3,0], [3,2], and [2,2].
Using points [1,0], [3,0], [3,2], and [2,2].
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one horizontal trapezoid that can be formed.

 

Constraints:

4 <= points.length <= 105
–108 <= xi, yi <= 108
All points are pairwise distinct.©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, points: List[List[int]]) -> int:
        ### Time Limit Exceeded 553 / 554 testcases passed
        dy = defaultdict(int)
        for x,y in points:
            dy[y] += 1
        # county = []
        # for each in dy:
        #     if dy[each] > 1:
        #         county.append(dy[each]*(dy[each]-1)//2)
        count2 = 0
        for each in dy:
            if dy[each] > 1:
                count2 += 1
        if count2 < 2:
            return 0
            
        county = [0]*count2
        sumy = [0]*count2
        index = 0
        for each in dy:
            if dy[each] > 1:
                county[index] = dy[each]*(dy[each]-1)//2
                index += 1
                
        #county = list(dy.values())
        ll = len(county)
        sumy[-1] = county[-1]
        for ii in range(ll-2, -1,-1):
            sumy[ii] = county[ii]+sumy[ii+1]
        # for ii in range(ll):
        #     county[ii] = county[ii]*(county[ii]-1)//2
        result = 0

        for ii in range(ll-1):
            #for jj in range(ii+1,ll):
            result += county[ii] * sumy[ii+1]
        return result%(10**9+7)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
