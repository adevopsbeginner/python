"""
Q2. Minimum Swaps to Sort by Digit Sum
Medium
4 pt.
You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

Return the minimum number of swaps required to rearrange nums into this sorted order.

A swap is defined as exchanging the values at two distinct positions in the array.

 

Example 1:

Input: nums = [37,100]

Output: 1

Explanation:

Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 1.
Example 2:

Input: nums = [22,14,33,7]

Output: 0

Explanation:

Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
Thus, the minimum number of swaps required to rearrange nums is 0.
Example 3:

Input: nums = [18,43,34,16]

Output: 2

Explanation:

Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
nums consists of distinct positive integers.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        def digits(num: int):
            result = 0
            while num:
                result += num%10
                num //=10
            return result
            
        ll = len(nums)
        for ii in range(ll):
            nums[ii] = [digits(nums[ii]), nums[ii], ii]
        nums.sort()
        for ii in range(ll):
            nums[ii] = nums[ii][2]
        #print(nums)

        index_after_sort = [0]*ll
        for ii in range(ll):
            index_after_sort[nums[ii]] = ii
        #print(index_after_sort)

        result = 0
        for ii in range(ll):
            #print(ii, nums, index_after_sort)
            if ii == nums[ii]:
                continue
            nums[index_after_sort[ii]] = nums[ii]
            index_after_sort[nums[ii]] = index_after_sort[ii]
            index_after_sort[ii] = ii
            nums[ii] = ii
            result += 1
            #print(ii, nums)

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
