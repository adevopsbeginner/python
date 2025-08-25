"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
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
    def leetcode(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ll = len(nums)
        result = []

        for ii in range(ll-2):
            if nums[ii] > 0:
                break

            ## skip duplicated ii
            if ii > 0 and nums[ii] == nums[ii-1]:
                continue
            index3 = ll-1
            for jj in range(ii+1, ll-1):
                ## skip duplicated jj
                if jj-ii > 1 and nums[jj] == nums[jj-1]:
                    continue
                iijj = 0-(nums[ii]+nums[jj])
                if iijj < 0:
                    break

                while index3 > jj and nums[index3] > iijj:
                    index3 -= 1
                
                if index3 <= jj:
                    break
                
                if nums[index3] == iijj:
                    result.append([nums[ii], nums[jj], iijj])
                    ## skip duplicated kk
                    while index3 > 0 and nums[index3] == nums[index3-1]:
                        index3 -= 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
