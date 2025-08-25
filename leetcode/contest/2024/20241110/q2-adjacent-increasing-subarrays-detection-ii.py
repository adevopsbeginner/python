"""

Code
Testcase
Test Result
Test Result
Q2. Adjacent Increasing Subarrays Detection II
Medium
5 pt.
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
 

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        ll = len(nums)
        k = 1
        a = 0
        a_increase = 1
        for ii in range(a+1,ll):
            if nums[ii] > nums[ii-1]:
                if ii == ll-1:
                    k = max(k,(ii-a+1)//2)
                    return k
            else:
                a_increase = ii-a
                print(111,a,ii,k,a_increase)
                k = max(k,a_increase//2)
                #print(a,ii, a_increase)
                a = ii
                b = ii

                print(222,a,ii,k,a_increase)
                for jj in range(1,ll-b):
                    print(a,ii,b,jj,k,a_increase)
                    if nums[b+jj] <= nums[b+jj-1]:
                        k = max(k,min(a_increase,jj))
                        a = b+jj
                        k = max(k,(jj+1)//2)
                        a_increase = jj+1
                        break
                    else:
                        if jj == ll-b-1:
                            k = max(k,min(a_increase,jj+1))
                            return k

        return k

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
