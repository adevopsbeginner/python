"""
836. Rectangle Overlap
Easy
Topics
Companies
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.



Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false


Constraints:

rec1.length == 4
rec2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1 and rec2 represent a valid rectangle with a non-zero area.
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
    def leetcode(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0]:
            return False
        if rec2[1] >= rec1[3] or rec2[3] <= rec1[1]:
            return False
        return True

        ### wrong answer
        if rec2[0] > rec1[0] and rec2[0] < rec1[2]:
            if rec2[1] > rec1[1] and rec2[1] < rec1[3]:
                return True
            if rec2[3] > rec1[1] and rec2[3] < rec1[3]:
                return True
        if rec2[2] > rec1[0] and rec2[2] < rec1[2]:
            if rec2[1] > rec1[1] and rec2[1] < rec1[3]:
                return True
            if rec2[3] > rec1[1] and rec2[3] < rec1[3]:
                return True

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
