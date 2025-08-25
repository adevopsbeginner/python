'''
1863. Sum of All Subset XOR Totals
Easy
Topics
Companies
Hint
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.



Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
Example 3:

Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.


Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
'''

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        total_xor_sum = 0
        ll = len(nums)

        ### The total number of subsets of an array of length n is 2^n
        ### We use the bitwise representation of numbers from 0 to 2^n - 1 to represent each subset
        for ii in range(1 << ll):
            subset_xor = 0

            ### Each bit in the number i represents whether the corresponding element in nums is included in the subset or not.
            for jj in range(ll):
                if ii & (1 << jj):
                    subset_xor ^= nums[jj]
            total_xor_sum += subset_xor
        return total_xor_sum

        result = [[]]
        for each in nums:
            ll = len(result)
            for ii in range(ll):
                result.append(result[ii]+[each])

        xor = 0
        for each in result:
            if len(each) == 0:
                continue
            elif len(each) == 1:
                xor += each[0]
            else:
                xor += reduce(lambda a, b: a^b, each)

        return xor

if __name__ == "__main__":
    app = Solution()
    a = 2
    print(app.leetcode(a))
