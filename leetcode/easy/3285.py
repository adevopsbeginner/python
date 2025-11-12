"""
3285. Find Indices of Stable Mountains
Easy
Topics
premium lock icon
Companies
There are n mountains in a row, and each mountain has a height. You are given an integer array height where height[i] represents the height of mountain i, and an integer threshold.

A mountain is called stable if the mountain just before it (if it exists) has a height strictly greater than threshold. Note that mountain 0 is not stable.

Return an array containing the indices of all stable mountains in any order.

 

Example 1:

Input: height = [1,2,3,4,5], threshold = 2

Output: [3,4]

Explanation:

Mountain 3 is stable because height[2] == 3 is greater than threshold == 2.
Mountain 4 is stable because height[3] == 4 is greater than threshold == 2.
Example 2:

Input: height = [10,1,10,1,10], threshold = 3

Output: [1,3]

Example 3:

Input: height = [10,1,10,1,10], threshold = 10

Output: []

 

Constraints:

2 <= n == height.length <= 100
1 <= height[i] <= 100
1 <= threshold <= 100
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
    def leetcode(self, height: List[int], threshold: int) -> List[int]:
        result = []
        ll = len(height)
        for ii in range(ll-1):
            if height[ii] > threshold:
                result.append(ii+1)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
