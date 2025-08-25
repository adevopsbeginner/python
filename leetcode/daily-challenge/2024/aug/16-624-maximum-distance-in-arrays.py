"""
624. Maximum Distance in Arrays
Medium
Topics
Companies
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.



Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0


Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
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
    def leetcode(self, arrays: List[List[int]]) -> int:
        ### chatgpt
        min_value = arrays[0][0]  # Smallest value so far
        max_value = arrays[0][-1] # Largest value so far
        max_distance = 0          # Max distance found so far

        for i in range(1, len(arrays)):
            current_array = arrays[i]
            current_min = current_array[0]
            current_max = current_array[-1]

            # Calculate possible max distances
            max_distance = max(max_distance, abs(current_max - min_value), abs(max_value - current_min))

            # Update min_value and max_value for future comparisons
            min_value = min(min_value, current_min)
            max_value = max(max_value, current_max)

        return max_distance

        ### time limit exceeded
        m = len(arrays)
        result = 0
        maxarray = [0] * m
        minarray = [0] * m
        for ii in range(m):
            maxarray[ii] = arrays[ii][-1]
            minarray[ii] = arrays[ii][0]
        for ii in range(m-1):
            for jj in range(ii+1,m):
                result = max(result, abs(maxarray[ii]-minarray[jj]))
                result = max(result, abs(maxarray[jj]-minarray[ii]))

        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
