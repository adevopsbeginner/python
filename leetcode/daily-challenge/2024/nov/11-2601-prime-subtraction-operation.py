"""
2601. Prime Subtraction Operation
Attempted
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:

Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].
Return true if you can make nums a strictly increasing array using the above operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater than its preceding element.

 

Example 1:

Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.
Example 2:

Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.
Example 3:

Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
nums.length == n
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
    def leetcode(self, nums: List[int]) -> bool:
        prime = [2,3,5,7]
        for ii in range(11,1001):
            if ii % 2 and ii % 3 and ii % 5:
                is_prime = 1
                for jj in range(2,min(ii, 100)):
                    if ii%jj == 0:
                        is_prime = 0
                if is_prime:
                    prime.append(ii)
        #print(prime)
        print(len(prime))

        ll = len(nums)
        if ll == 1:
            return True
        for ii in range(ll-2,-1,-1):
            if nums[ii] < nums[ii+1]:
                continue
            for each in prime:
                #print(each,nums[ii],nums[ii+1])
                if each >= nums[ii]:
                    return False
                if nums[ii]-each < nums[ii+1]:
                    nums[ii] -= each
                    break
                if each == prime[-1]:
                    return False
                
            #print(nums)
        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
