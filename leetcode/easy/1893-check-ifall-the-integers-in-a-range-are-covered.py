"""
1893. Check if All the Integers in a Range Are Covered
Easy
Topics
Companies
Hint
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

 

Example 1:

Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
Example 2:

Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.
 

Constraints:

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
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
    def leetcode(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        start,end = ranges.pop(0)
        q = [[start,end]]

        while len(ranges):
            start,end = ranges.pop(0)
            if start > q[-1][1]+1:
                q.append([start,end])
            else:
                q[-1][1] = max(end, q[-1][1])
        #print(q)
        for start,end in q:
            if left > end:
                continue
            if left < start:
                return False
            if right <= end:
                return True
        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
