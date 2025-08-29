"""
56. Merge Intervals
Solved
Medium
Topics
￼
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
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
    def leetcode(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ll = len(intervals)
        if ll == 0:
            return 0
        if ll == 1:
            return intervals
        start,end = intervals[0]
        ans = []
        for ii in range(1,ll):
            if intervals[ii][0] <= end:
                end = max(end,intervals[ii][1])
            else:
                ans.append([start,end])
                start,end = intervals[ii]
        ans.append([start,end])
            
        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
