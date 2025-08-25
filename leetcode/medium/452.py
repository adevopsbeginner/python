"""
452. Minimum Number of Arrows to Burst Balloons
Solved
Medium
Topics
premium lock icon
Companies
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
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
    def leetcode(self, points: List[List[int]]) -> int:
        ll = len(points)
        if ll < 2:
            return ll

        ### 1. indecies

        points.sort()

        ### balloons that not burst
        first = [[x[0],ii] for ii, x in enumerate(points)]
        ### shooting point
        second = [[x[1],ii] for ii, x in enumerate(points)]

        ### 2. sort
        second.sort()
        
        result = 0

        ### 3. shoot arrows
        current = 0
        for ii in range(ll):
            #print(ii, first)
            #print(ii, second)
            #print(ii, second[ii][1], first[second[ii][1]])
            ### we only shoot balloons that has not been burst
            if first[second[ii][1]][1] >= 0:
                result += 1

                ### burst all balloons before this current ballons
                #print(ii, current, first[current][0], second[ii][0])
                while first[current][0] <= second[ii][0]:
                    first[current][1] = -1
                    current += 1

                    if current >= ll:
                        return result

        return result

        ### time limit exceeded
        ll = len(points)
        if ll < 2:
            return ll
        points0 = sorted(points)
        points.sort(key=lambda x:x[1])
        ans = []
        while len(points):
            c1 = points.pop(0)
            ans.append(c1[1])
            while len(points0):
                if points0[0][0] <= c1[1]:
                    c0 = points0.pop(0)
                    if c0 in points:
                        points.remove(c0)
                else:
                    break

        return len(ans)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
