"""
941. Valid Mountain Array
Solved
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
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
    def leetcode(self, arr: List[int]) -> bool:
        ll = len(arr)
        if ll < 3:
            return False

        if arr[1] <= arr[0]:
            return False

        if arr[-2] <= arr[-1]:
            return False

        flag = 0
        for ii in range(2,ll):
            if flag == 0:
                if arr[ii] == arr[ii-1]:
                    return False
                elif arr[ii] < arr[ii-1]:
                    flag = 1
            else:
                if arr[ii] >= arr[ii-1]:
                    return False

        if flag == 0:
            return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
