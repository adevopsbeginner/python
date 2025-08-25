"""
494. Target Sum
Attempted
Medium
Topics
Companies
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
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
    def leetcode(self, nums: List[int], target: int) -> int:
        # Memoization dictionary to store (index, current_sum) => ways
        memo = {}
        
        def backtrack(index, current_sum):
            # Base case: if we have processed all numbers
            if index == len(nums):
                return 1 if current_sum == target else 0
            
            # Check if result is already in memo
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Explore adding '+' and '-' for the current number
            add = backtrack(index + 1, current_sum + nums[index])
            subtract = backtrack(index + 1, current_sum - nums[index])
            
            # Store the result in memo
            memo[(index, current_sum)] = add + subtract
            return memo[(index, current_sum)]
        
        # Start the recursion
        return backtrack(0, 0)

        ### time limit exceeded
        result = 0
        ll = len(nums)
        nums.sort(reverse=True)
        sumnums = [0]*ll
        sumnums[0] = sum(nums)-nums[0]
        for ii in range(1,ll):
            sumnums[ii] = sumnums[ii-1] - nums[ii]
        bits = 0
        while bits < 2**ll:
            cal = 0
            for ii in range(ll):
                if bits & (1<<(ll-1-ii)) == 0:
                    cal += nums[ii]
                else:
                    cal -= nums[ii]

                if cal + sumnums[ii] < target:
                    bits += (1<<(ll-1-ii)) - 1
                    break
                elif cal - sumnums[ii] > target:
                    bits += (1<<(ll-1-ii)) - 1
                    break

            #print(cal)
            if cal == target:
                result += 1

            bits += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
