"""

Code
Testcase
Test Result
Test Result
2535. Difference Between Element Sum and Digit Sum of an Array
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Explanation:
The element sum of nums is 1 + 2 + 3 + 4 = 10.
The digit sum of nums is 1 + 2 + 3 + 4 = 10.
The absolute difference between the element sum and digit sum is |10 - 10| = 0.
 

Constraints:

1 <= nums.length <= 2000
1 <= nums[i] <= 2000
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
        def digit_sum_cal(num):
            result = 0
            for each in [10000,1000,100,10]:
                result += num//each
                num %= each
            result += num
            #print(num, result)
            return result

        element_sum = sum(nums)
        digit_sum = 0
        for each in nums:
            digit_sum += digit_sum_cal(each)

        return abs(element_sum-digit_sum)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
