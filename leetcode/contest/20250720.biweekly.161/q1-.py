"""
Q1. Split Array by Prime Indices
Medium
4 pt.
You are given an integer array nums.

Split nums into two arrays A and B using the following rule:

Elements at prime indices in nums must go into array A.
All other elements must go into array B.
Return the absolute difference between the sums of the two arrays: |sum(A) - sum(B)|.

A prime number is a natural number greater than 1 with only two factors, 1 and itself.

Note: An empty array has a sum of 0.

 

Example 1:

Input: nums = [2,3,4]

Output: 1

Explanation:

The only prime index in the array is 2, so nums[2] = 4 is placed in array A.
The remaining elements, nums[0] = 2 and nums[1] = 3 are placed in array B.
sum(A) = 4, sum(B) = 2 + 3 = 5.
The absolute difference is |4 - 5| = 1.
Example 2:

Input: nums = [-1,5,7,0]

Output: 3

Explanation:

The prime indices in the array are 2 and 3, so nums[2] = 7 and nums[3] = 0 are placed in array A.
The remaining elements, nums[0] = -1 and nums[1] = 5 are placed in array B.
sum(A) = 7 + 0 = 7, sum(B) = -1 + 5 = 4.
The absolute difference is |7 - 4| = 3.
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, nums: List[int]) -> int:
        def is_prime(num):
            if num == 0:
                return False
            if num == 1:
                return False
            if num == 2:
                return True
            if num == 3:
                return True
            if num == 4:
                return False
            if num < 100:
                for ii in range(2, num//2+1):
                    if num%ii == 0:
                        return False
            else:
                for ii in range(3, math.floor(math.sqrt(num))+1,2):
                    if num%ii == 0:
                        return False
            return True

        #print(-602741550-243097563-435785956+567926486-462415908)
                
        sum_nums = sum(nums)
        sum_prime = 0
        ll = len(nums)
        for ii in range(2,ll):
            if ii < 2:
                continue
            elif ii == 2 or ii == 3:
                sum_prime += nums[ii]
            elif ii%2 == 0  or ii%3 == 0:
                continue
            elif is_prime(ii):
                #print(ii)
                sum_prime += nums[ii]
                
        return abs(sum_nums-sum_prime-sum_prime)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
