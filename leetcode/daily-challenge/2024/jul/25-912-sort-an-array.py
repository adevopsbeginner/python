"""
912. Sort an Array
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
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
    def leetcode(self, nums: List[int]) -> List[int]:
        def mergesubarray(nums1: List[int], nums2: List[int]) -> List[int]:
            ll1 = len(nums1)
            ll2 = len(nums2)
            if ll1 == 0:
                return nums2
            if ll2 == 0:
                return nums1
            index1 = 0
            index2 = 0
            result = [0] * (ll1+ll2)
            while index1 < ll1 and index2 < ll2:
                if nums1[index1] < nums2[index2]:
                    result[index1 + index2] = nums1[index1]
                    index1 += 1
                else:
                    result[index1 + index2] = nums2[index2]
                    index2 += 1
            if index1 == ll1:
                for ii in range(ll2-index2):
                    result[ll1+index2+ii] = nums2[index2+ii]
            if index2 == ll2:
                for ii in range(ll1-index1):
                    result[ll2+index1+ii] = nums1[index1+ii]

            # print("C", result)
            return result

        def mergearray(k: int) -> List[int]:
            for ii in range(ll//(2*k)+1):
                start1 = ii*(2*k)
                start2 = ii*(2*k) + k
                if start1 >= ll:
                    continue
                if start2 >= ll:
                    continue
                end2 = min(ll, ii*(2*k) + k + k)

                index = 0
                # print(start1,start2,end2)
                for each in mergesubarray(nums[start1:start2], nums[start2:end2]):
                    nums[start1+index] = each
                    index += 1
            # print("B",nums)

            return nums

        ll = len(nums)
        mergesort = 1
        while mergesort < ll:
            mergearray(mergesort)
            # print("A",nums)
            mergesort *= 2

        return nums


if __name__ == "__main__":
    app = Solution()
    a = [5,2,3,1]
    print(app.leetcode(a))
