"""
2540. Minimum Common Value
Easy
Topics
premium lock icon
Companies
Hint
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
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
    def leetcode(self, nums1: List[int], nums2: List[int]) -> int:
        ll1 = len(nums1)
        ll2 = len(nums2)
        index1 = 0
        index2 = 0
        while index1 < ll1 and index2 < ll2:
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            if nums1[index1] < nums2[index2]:
                index1 += 1
                continue
            if nums1[index1] > nums2[index2]:
                index2 += 1
                continue
        return -1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
