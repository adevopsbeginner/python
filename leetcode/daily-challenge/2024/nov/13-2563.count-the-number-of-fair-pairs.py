"""
2563. Count the Number of Fair Pairs
Medium
Topics
Companies
Hint
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
 

Constraints:

1 <= nums.length <= 105
nums.length == n
-109 <= nums[i] <= 109
-109 <= lower <= upper <= 109
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
    def leetcode(self, nums: List[int], lower: int, upper: int) -> int:
        ### chatgpt
        # Sort the array
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n):
            # Use binary search to find the range of valid pairs
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            count += (right - left)

        return count

        ### time exceeded
        ll = len(nums)
        result = 0
        dd = defaultdict(int)
        for each in nums:
            dd[each] += 1

        lldd = list(dd.keys())
        lldd.sort()
        #print(lldd)
        ll = len(lldd)

        for ii in range(ll):
            if lldd[ii]*2 >= lower and lldd[ii]*2 <= upper:
                result += (dd[lldd[ii]]-1)*(dd[lldd[ii]])//2

        for ii in range(ll-1):
            #print(ii)
            if upper > 0 and lldd[ii] > upper:
                break
            for jj in range(ii+1, ll):
                #print(ii,jj)
                if lldd[ii] + lldd[jj] > upper:
                    break
                if lldd[ii] + lldd[jj] >= lower:
                    result += dd[lldd[ii]] * dd[lldd[jj]]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
