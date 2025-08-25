"""
539. Minimum Time Difference
Solved
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
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
    def leetcode(self, timePoints: List[str]) -> int:
        ll = len(timePoints)
        timePoints.sort()
        minutes = [0] * ll
        for ii in range(ll):
            t = timePoints[ii]
            minutes[ii] = int(t[0:2])*60 + int(t[3:])
        result = minutes[0] - minutes[-1] + 24*60
        for ii in range(1, ll):
            result = min(result, minutes[ii]-minutes[ii-1])

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
