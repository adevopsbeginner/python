"""
165. Compare Version Numbers
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
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
    def leetcode(self, version1: str, version2: str) -> int:
        v1list = [int(each) for each in version1.split(".")]
        v2list = [int(each) for each in version2.split(".")]


        while len(v1list) > 0 and v1list[-1] == 0:
            v1list.pop()
        while len(v2list) > 0 and v2list[-1] == 0:
            v2list.pop()
        
        ll1 = len(v1list)
        ll2 = len(v2list)
        for ii in range(min(ll1, ll2)):
            if v1list[ii] < v2list[ii]:
                return -1
            elif v1list[ii] > v2list[ii]:
                return 1
        
        if ll1 == ll2:
            return 0
        if ll1 < ll2:
            return -1
        if ll1 > ll2:
            return 1

        return 0


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
