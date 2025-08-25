"""
179. Largest Number
Solved
Medium
Topics
Companies
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
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
    def leetcode(self, nums: List[int]) -> str:
        # Convert all numbers to string for concatenation purposes
        nums_str = list(map(str, nums))

        # Custom comparator that compares the two possible concatenations
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Sort the numbers based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Join the numbers to form the largest number
        largest_num = ''.join(nums_str)

        # Edge case: when the result is something like "000", return "0" instead
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
