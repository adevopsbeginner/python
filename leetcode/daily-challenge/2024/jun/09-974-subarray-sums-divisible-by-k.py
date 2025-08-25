"""

Code
Testcase
Test Result
Test Result
974. Subarray Sums Divisible by K
Medium
Topics
Companies
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0


Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int], k: int) -> int:
        ll = len(nums)
        result = 0

        prefix_sum = 0
        remainder_count = {0: 1}
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k

            # If this remainder has been seen before, it means there's a subarray
            # ending here which sums to a multiple of k
            if remainder in remainder_count:
                count += remainder_count[remainder]
                print("yes",num,remainder,count,remainder_count)
            else:
                print("no ",num,remainder,count,remainder_count)

            # Update the count of this remainder
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

        ### Time Limit Exceeded
        for ii in range(ll):
            sum0 = 0
            for jj in range(ii,ll):
                sum0 += nums[jj]
                if sum0 % k == 0:
                    # print(nums[ii:jj+1])
                    result += 1
        return result

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,-2,-3,1]
    # a = [-5]
    k = 5
    print(app.leetcode(a,k))
