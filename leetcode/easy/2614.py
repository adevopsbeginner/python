"""
2614. Prime In Diagonal
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1] = val.


In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

 

Example 1:

Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
Example 2:

Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
 

Constraints:

1 <= nums.length <= 300
nums.length == numsi.length
1 <= nums[i][j] <= 4*106
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
    def leetcode(self, nums: List[List[int]]) -> int:
        def isprime(num):
            if num == 1:
                return False
            if num == 2:
                return True

            for ii in range(2, math.floor(math.sqrt(num))+1):
                if num%ii == 0:
                    return False
            return True

        ll = len(nums)
        result = 0
        for rr in range(ll):
            for cc in range(ll):
                if rr == cc or cc == ll-rr-1:
                    if isprime(nums[rr][cc]):
                        result = max(result, nums[rr][cc])
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
