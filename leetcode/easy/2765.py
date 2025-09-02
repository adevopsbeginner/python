"""
2765. Longest Alternating Subarray
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums. A subarray s of length m is called alternating if:

m is greater than 1.
s1 = s0 + 1.
The 0-indexed subarray s looks like [s0, s1, s0, s1,...,s(m-1) % 2]. In other words, s1 - s0 = 1, s2 - s1 = -1, s3 - s2 = 1, s4 - s3 = -1, and so on up to s[m - 1] - s[m - 2] = (-1)m.
Return the maximum length of all alternating subarrays present in nums or -1 if no such subarray exists.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,3,4,3,4]

Output: 4

Explanation:

The alternating subarrays are [2, 3], [3,4], [3,4,3], and [3,4,3,4]. The longest of these is [3,4,3,4], which is of length 4.

Example 2:

Input: nums = [4,5,6]

Output: 2

Explanation:

[4,5] and [5,6] are the only two alternating subarrays. They are both of length 2.

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 104
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
        result = -1
        index0 = 0
        index1 = 1
        flag = 1
        for ii in range(1,ll):
            #print(ii, result, index0, index1, flag, nums[ii-1], nums[ii])
            if nums[index1] == nums[index0]+1:
                if ii == index1:
                    if ii == ll-1:
                        result = max(result, ll-index0)
                        break
                    flag = -1
                    continue
                if nums[ii] == nums[ii-1]+flag:
                    if ii == ll-1:
                        result = max(result, ll-index0)
                        break
                    flag *= -1
                    continue
                else:
                    result = max(result, ii-index0)
                    index0 = ii-1
                    index1 = ii
                    flag = -1
            else:
                index0 += 1
                index1 += 1
                flag = -1
            #print(index0, index1, result)

        #result = max(result, ll-index0)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
