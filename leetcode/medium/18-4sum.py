"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
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
    def leetcode(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        ll = len(nums)

        for ii in range(ll-3):
            if ii > 0 and nums[ii] == nums[ii-1]:
                continue
            for jj in range(ii+1, ll-2):
                if jj > ii+1 and nums[jj] == nums[jj-1]:
                    continue
                ### 2 pointers
                left,right = jj+1, ll-1
                while left < right:
                    #print(ii,jj,left,right,target, result)
                    total = nums[ii]+nums[jj]+nums[left]+nums[right]
                    #print(ii,jj,left,right, nums[ii], nums[jj], nums[left], nums[right], total, target)
                    

                    if total == target:
                        #print(ii,jj,left,right, nums[ii], nums[jj], nums[left], nums[right])
                        result.append([nums[ii], nums[jj], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

        ### time limit exceeded
        for ii in range(ll-3):
            for jj in range(ii+1, ll-2):
                for kk in range(jj+1, ll-1):
                    for mm in range(kk+1, ll):
                        #print(nums[ii], nums[jj], nums[kk], nums[mm])
                        if nums[ii]+nums[jj]+nums[kk]+nums[mm] == target:
                            if [nums[ii], nums[jj], nums[kk], nums[mm]] not in result:
                                result.append([nums[ii], nums[jj], nums[kk], nums[mm]])
                            break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
