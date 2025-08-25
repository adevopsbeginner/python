"""
1365. How Many Numbers Are Smaller Than the Current Number
Easy
Topics
Companies
Hint
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
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
    def leetcode(self, nums: List[int]) -> List[int]:
        ll = len(nums)
        matrix = [[nums[ii],ii,0] for ii in range(ll)]
        #print(matrix)
        matrix.sort()
        #print(matrix)
        matrix[0][2] = 0
        for ii in range(1,ll):
            if matrix[ii][0] > matrix[ii-1][0]:
                matrix[ii][2] = ii
            else:
                matrix[ii][2] = matrix[ii-1][2]
        matrix.sort(key=lambda x:x[1])
        #print(matrix)
        for ii in range(ll):
            nums[ii] = matrix[ii][2]

        return nums


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
