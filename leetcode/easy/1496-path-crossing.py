"""
1496. Path Crossing
Solved
Easy
Topics
Companies
Hint
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
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
    def leetcode(self, path: str) -> bool:
        xx = 0
        yy = 0
        ll = len(path)
        been = defaultdict(list)
        been[0].append(0)
        for ii in range(ll):
            if path[ii] == "N":
                yy += 1
            elif path[ii] == "S":
                yy -= 1
            elif path[ii] == "E":
                xx += 1
            elif path[ii] == "W":
                xx -= 1
            if yy in been[xx]:
                return True
            been[xx].append(yy)

        return False


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
