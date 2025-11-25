"""
3364. Minimum Positive Sum Subarray 
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray. If no such subarray exists, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 

Constraints:

1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000
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
    def leetcode(self, nums: List[int], l: int, r: int) -> int:
        if max(nums) <= 0:
            return -1
        # if l == r == 1:
        #     return min(nums)

        result = -1
        ll = len(nums)
        lsum = sum(nums[0:l-1])
        lr = r-l+1
        for ii in range(ll-l+1):
            #print(ii,l,r,lsum)
            lrsum = lsum
            lsum += nums[ii+l-1]
            for jj in range(lr):
                #print(ii,jj,lsum,lrsum, result)
                if ii+l+jj > ll:
                    break
                lrsum += nums[ii+l+jj-1]
            
                if lrsum == 1:
                    return 1
                if lrsum > 0:
                    if result > 0:
                        result = min(result, lrsum)
                    else:
                        result = lrsum

            lsum -= nums[ii]

        return result



if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
