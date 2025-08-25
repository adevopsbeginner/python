"""
100329. Minimum Operations to Make Array Equal to Target
Hard
You are given two positive integer arrays nums and target, of the same length.

In a single operation, you can select any
subarray
 of nums and increment or decrement each element within that subarray by 1.

Return the minimum number of operations required to make nums equal to the array target.



Example 1:

Input: nums = [3,5,1,2], target = [4,6,2,4]

Output: 2

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..3] by 1, nums = [4,6,2,3].
- Increment nums[3..3] by 1, nums = [4,6,2,4].

Example 2:

Input: nums = [1,3,2], target = [2,1,4]

Output: 5

Explanation:

We will perform the following operations to make nums equal to target:
- Increment nums[0..0] by 1, nums = [2,3,2].
- Decrement nums[1..1] by 1, nums = [2,2,2].
- Decrement nums[1..1] by 1, nums = [2,1,2].
- Increment nums[2..2] by 1, nums = [2,1,3].
- Increment nums[2..2] by 1, nums = [2,1,4].



Constraints:

1 <= nums.length == target.length <= 105
1 <= nums[i], target[i] <= 108
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int], target: List[int]) -> int:
        ## not working, have not finished
        ll = len(nums)
        result = 0
        ld = [nums[ii]-target[ii] for ii in range(ll)]

        if ll == 0:
            return 0
        if ll == 1:
            return abs(ld[0])

        print(ld)
        ldd = [ld[0]]
        for ii in range(1, ll):
            if ld[ii] != ld[ii-1]:
                ldd.append(ld[ii])
        print(ldd)

        ll = len(ldd)

        if ldd[0] > 0 and ldd[0] > ldd[1]:
            print(ldd[0], ldd[1])
            result += ldd[0]
        if ldd[0] < 0 and ldd[0] < ldd[1]:
            print(ldd[0], ldd[1])
            result -= ldd[0]

        if ldd[-1] > 0 and ldd[-1] > ldd[-2]:
            print(ldd[-2], ldd[-1])
            result += ldd[-1]
        if ldd[-1] < 0 and ldd[-1] < ldd[-2]:
            print(ldd[-2], ldd[-1])
            result -= ldd[-1]

        for ii in range(1,ll-1):
            if ldd[ii] > 0 and ldd[ii] > ldd[ii-1] and ldd[ii] > ldd[ii+1]:
                print(ldd[ii-1], ldd[ii], ldd[ii+1])
                result += ldd[ii]
            if ldd[ii] < 0 and ldd[ii] < ldd[ii-1] and ldd[ii] < ldd[ii+1]:
                print(ldd[ii - 1], ldd[ii], ldd[ii + 1])
                result -= ldd[ii]

        return result

if __name__ == "__main__":
    app = Solution()
    nums = [5,9,2,2]
    target = [7,9,3,8]
    print(app.leetcode(nums,target))
