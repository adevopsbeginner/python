"""
2293. Min Max Game
Easy
Topics
Companies
Hint
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.

 

Example 1:


Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
Example 2:

Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.
 

Constraints:

1 <= nums.length <= 1024
1 <= nums[i] <= 109
nums.length is a power of 2.
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
        base = 1
        ll = len(nums)
        ll2 = ll
        while base < ll:
            flag = 0
            ll2 //= 2
            for ii in range(ll2):
                ii1 = ii*2*base
                ii2 = ii1+base
                #print(ii, base, ii1, ii2)
                if flag == 0:
                    if nums[ii1] > nums[ii2]:
                        nums[ii1], nums[ii2] = nums[ii2], nums[ii1]
                    flag = 1
                elif flag == 1:
                    if nums[ii1] < nums[ii2]:
                        nums[ii1], nums[ii2] = nums[ii2], nums[ii1]
                    flag = 0
            base *= 2
            print(nums)

        return nums[0]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
