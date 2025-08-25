'''
136. Single Number
Solved
Easy
Topics
Companies
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

        ## 136ms, 19.12MB
        nums.sort()
        ll = len(nums)

        for ii in range(0,ll-1,2):
            if nums[ii] != nums[ii+1]:
                return nums[ii]

        return nums[-1]

if __name__ == "__main__":
    app = Solution()
    a = "A man, a plan, a canal, : Panama"
    a = ".,"
    a = "0P"
    print(app.leetcode(a))
