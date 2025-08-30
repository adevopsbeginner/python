"""
57. Insert Interval
Solved
Medium
Topics
￼
Companies
Hint
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
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
    def leetcode(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        ll = len(intervals)
        s,e = newInterval
        flag = 0
        
        if ll:
            if e < intervals[0][0]:
                return [newInterval]+intervals
            if s > intervals[-1][1]:
                return intervals+[newInterval]
        else:
            return [newInterval]
            
        for ii in range(ll):
            iis,iie = intervals[ii]
            if iie < s or iis > e:
                if iis > e and flag == 0:
                    ans.append(newInterval)
                    flag = 1
                ans.append(intervals[ii])
            else:
                if flag == 0:
                    s = min(iis,s)
                    e = max(iie,e)
                    ans.append([s,e])
                    flag = 1
                else:
                    ans[-1][1] = max(iie,e)

        return ans


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
