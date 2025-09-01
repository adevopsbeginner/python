"""
875. Koko Eating Bananas
Medium
Topics
premium lock icon
Companies
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
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
    def leetcode(self, piles: List[int], h: int) -> int:
        def is_valid(k):
            count = 0
            for pile in piles:
                count += pile//k
                if pile%k:
                    count += 1
            if count > h:
                return False
            return True

        low = 1
        high = max(piles)
        result = high

        while low <= high:
            if low == high:
                break

            if low+1 == high:
                if is_valid(low):
                    result = low
                    break
                else:
                    result = high
                    break

            if is_valid((low+high)//2):
                high = (low+high)//2
                result = high
            else:
                low = (low+high)//2

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
