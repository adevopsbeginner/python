"""

Code
Testcase
Testcase
Test Result
3097. Shortest Subarray With OR at Least K II
Solved
Medium
Topics
Companies
Hint
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty 
subarray
 of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.

 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 109
0 <= k <= 109
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
    def leetcode(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        ll = len(nums)
        result = ll + 1

        current_or = 0
        left = 0
        
        for right in range(ll):
            current_or |= nums[right]
            
            if current_or >= k:
                if left == right:
                    return 1
                result = min(result, right - left + 1)

                current_or = 0
                for ii in range(right,left,-1):
                    current_or |= nums[ii]
                    #print(111,result,left,ii,right,current_or,k)
                    if current_or >= k:
                        result = min(result, right - ii + 1)
                        left = ii
                        break

        if result > ll:
            return -1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
