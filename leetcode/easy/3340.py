"""
3340. Check Balanced String
Easy
Topics
premium lock icon
Companies
You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

 

Example 1:

Input: num = "1234"

Output: false

Explanation:

The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.
Example 2:

Input: num = "24123"

Output: true

Explanation:

The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
Since both are equal the num is balanced.
 

Constraints:

2 <= num.length <= 100
num consists of digits only
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
    def leetcode(self, num: str) -> bool:
        listnum = list(num)
        ll = len(num)
        for ii in range(ll):
            listnum[ii] = int(listnum[ii])
        even = 0
        odd = 0
        for ii in range(ll):
            if ii%2 == 0:
                even += listnum[ii]
            else:
                odd += listnum[ii]
        return even == odd


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
