"""
1399. Count Largest Group
Easy
Topics
Companies
Hint
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
 

Constraints:

1 <= n <= 104
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
    def leetcode(self, n: int) -> int:
        digits_group = [0]*37 ### group(9999) = 36
        for ii in range(n):
            digitsum = 0
            num = ii + 1
            while num > 0:
                digitsum += num%10
                num //= 10
            digits_group[digitsum] += 1
        
        result = 0
        #print(digits_group)
        largest = max(digits_group)
        for ii in range(32):
            if digits_group[ii] == largest:
                result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
