'''
35. Search Insert Position
Solved
Easy
Topics
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int], target: int) -> int:
        index = 0
        ll = len(nums)
        start = 0
        end = ll-1
        while start <= end:
            #print(target, start, end, index)
            if target <= nums[start]:
                return start
            if target > nums[end]:
                return end+1
            if start+1 == end:
                return end
            index = start+(end-start)//2
            if target == nums[index]:
                return index
            if target < nums[index]:
                end = index
            if target > nums[index]:
                start = index+1

        return index

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = [1]
    b = 5
    b = 2
    print(app.leetcode(a, b))
