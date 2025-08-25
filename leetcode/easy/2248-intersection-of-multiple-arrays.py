"""
2248. Intersection of Multiple Arrays
Easy
Topics
Companies
Hint
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
 

Constraints:

1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
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
    def leetcode(self, nums: List[List[int]]) -> List[int]:
        for num in nums:
            num.sort()
        nums.sort()
        ll = len(nums)
        result = []
        while True:
            #print(nums)
            ll0 = len(nums[0])
            if ll0 == 0:
                break
            q = nums[0].pop(0)
            present_in_all = True
            empty_list = False
            for ii in range(1, ll):
                while len(nums[ii]) > 0 and q > nums[ii][0]:
                    nums[ii].pop(0)
                
                if len(nums[ii]) == 0:
                    empty_list = True
                    present_in_all = False
                    break
                        
                if q == nums[ii][0]:
                    continue
                elif q < nums[ii][0]:
                    present_in_all = False

            if present_in_all:
                result.append(q)
            if empty_list:
                break
            
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
