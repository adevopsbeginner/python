"""
228. Summary Ranges
Solved
Easy
Topics
Companies
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
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
    def leetcode(self, nums: List[int]) -> List[str]:
        result = []
        ll = len(nums)
        a = 0
        b = 0
        for ii in range(1,ll):
            # print(a,ii)
            if a == ii:
                continue

            if nums[ii] == nums[ii-1]+1:
                pass
            elif nums[ii] > nums[ii-1]+1:
                if a == ii-1:
                    result.append(str(nums[a]))
                else:
                    result.append(str(nums[a])+"->"+str(nums[ii-1]))
                a = ii
            else:
                print("error")
        if a == ll-1:
            result.append(str(nums[a]))
        elif a < ll-1:
            result.append(str(nums[a])+"->"+str(nums[ll-1]))

        return result

if __name__ == "__main__":
    app = Solution()
    a = [0,1,2,4,5,7]
    print(app.leetcode(a))
