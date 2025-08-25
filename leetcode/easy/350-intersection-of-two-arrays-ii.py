"""

Code
Testcase
Test Result
Test Result
350. Intersection of Two Arrays II
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000


Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
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
    def leetcode(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ll1 = len(nums1)
        ll2 = len(nums2)
        i1 = 0
        i2 = 0
        result = []
        while i1 < ll1 and i2 < ll2:
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
                if i1 == ll1:
                    break
                if i2 == ll2:
                    break
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
        return result

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    print(app.leetcode(a,b))
