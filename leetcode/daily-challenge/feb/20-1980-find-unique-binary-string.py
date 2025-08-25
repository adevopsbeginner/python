"""
1980. Find Unique Binary String
Solved
Medium
Topics
Companies
Hint
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
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
    def leetcode(self, nums: List[str]) -> str:
        ll = len(nums)
        result = ""
        for binary in range(ll+1):
            a_string = ""
            for ii in range(ll):
                if binary & (1<<ii) == 0:
                    a_string += "0"
                else:
                    a_string += "1"
            if a_string not in nums:
                return a_string

        return "1"*ll


        ### wrong answer
        count0 = [0]*ll
        count1 = [0]*ll
        for num in nums:
            for ii in range(ll):
                if num[ii] == "0":
                    count0[ii] += 1
                else:
                    count1[ii] += 1

        for ii in range(ll):
            if count0[ii] < count1[ii]:
                result += "0"
            else:
                result += "1"
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
