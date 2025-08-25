"""
1726. Tuple with Same Product
Medium
Topics
Companies
Hint
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
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
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        dd = defaultdict(int)
        for ii in range(ll):
            for jj in range(ii+1,ll):
                dd[nums[ii]*nums[jj]] += 1
        result = 0
        for each in dd:
            result += dd[each]*(dd[each]-1)//2*8
        return result

        ll = len(nums)
        nums.sort()
        result = 0
        for ii in range(ll-3):
            for jj in range(ii+1, ll-2):
                if nums[jj]*nums[jj]//nums[ii] > nums[-1]:
                    break
                for kk in range(jj+1, ll-1):
                    jjkk = nums[jj]*nums[kk]
                    if jjkk % nums[ii]:
                        continue
                    jjkkii = jjkk//nums[ii]
                    if jjkkii > nums[-1]:
                        break
                    
                    if jjkkii in nums[kk+1:]:
                        result += 8
        return result

### third try failed at 35/37
### second try failed due to time limit exceeded
### first try failed due to time limit exceeded with O(n^4)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
