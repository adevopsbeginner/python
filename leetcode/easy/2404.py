"""
2404. Most Frequent Even Element
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 105
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
    def leetcode(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dd = defaultdict(int)
        for each in nums:
            if each%2 == 0:
                dd[each] += 1
        result = -1
        frequent = 0
        for each in dd:
            # if each == 1028 or each == 1676:
            #     print(each, dd[each], frequent, result)
            if dd[each] < frequent:
                continue

            if dd[each] == frequent:
                if each < result:        
                    result = each
            elif dd[each] > frequent:
                result = each

            frequent = dd[each]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
