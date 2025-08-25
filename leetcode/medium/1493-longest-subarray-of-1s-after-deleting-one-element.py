"""
1493. Longest Subarray of 1's After Deleting One Element
Solved
Medium
Topics
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
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
        ### 24 Aug 2025
        ll = len(nums)
        if sum(nums) == 0:
            return 0
        if sum(nums) == ll:
            return ll-1
        if sum(nums) == ll-1:
            return ll-1

        nums = [0]+nums+[0]
        ll += 2
        count1 = 0
        result = 0
        count_0_1 = 0
        for ii in range(1, ll):
            if nums[ii] == 1:
                count1 += 1
            else:
                #print(ii, result, count1, count_0_1)
                result = max(result, count1+count_0_1)
                count_0_1 = count1
                count1 = 0
        
        return result

        ### 2Mar2025
        ll = len(nums)

        if ll == sum(nums):
            return ll-1
        if ll == sum(nums)-1:
            return ll
        if sum(nums) == 0:
            return 0

        nums.append(0)
        ll += 1

        result = 0
        first0 = -1
        count0 = 0
        front = 0
        end = 0

        while front < ll and end < ll:
            #print(result, front,end, count0,first0)
            if nums[end] == 0:
                if first0 == -1:
                    first0 = end
                count0 += 1
                if count0 > 1:
                    count = end-front
                    if first0 >= 0:
                        count -= 1
                    result = max(result, count)
                    front = first0 + 1
                    first0 = end
            end += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
