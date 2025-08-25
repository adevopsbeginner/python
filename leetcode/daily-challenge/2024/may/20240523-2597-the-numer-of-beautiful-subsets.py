'''
2597. The Number of Beautiful Subsets
Medium
Topics
Companies
Hint
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.



Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].


Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
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
    def leetcode(self, nums: List[int], k: int) -> int:
        ll = len(nums)
        result = 0
        for ii in range(1 << ll):
            subset = []
            beautiful = True
            for jj in range(ll):
                if ii & ( 1 << jj ):
                    if nums[jj]+k in subset or nums[jj]-k in subset:
                        beautiful = False
                        break
                    subset.append(nums[jj])
            if beautiful and len(subset):
                result += 1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [51, 15, 61, 64, 53, 6, 3, 5, 76, 79, 67, 26, 87, 76, 54, 50, 42, 80, 79]
    k = 74
    print(app.leetcode(a, k))
