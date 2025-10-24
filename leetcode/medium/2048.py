"""
2048. Next Greater Numerically Balanced Number
Medium
Topics
premium lock icon
Companies
Hint
An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106
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
        digits = [1,2,3,4,5,6]
        balanced_numbers = set()
        balanced_numbers.add(1224444)
        for r in range(1, len(digits)+1):
            for comb in itertools.combinations(digits, r):
                s = []
                total_len = 0
                for d in comb:
                    s += [str(d)]*d
                    total_len += d
                if total_len > 7:
                    continue
                
                for p in set(itertools.permutations(s)):
                    num = int("".join(p))
                    if num < 1224444:
                        balanced_numbers.add(num)

        for b in sorted(balanced_numbers):
            if b > n:
                return b
        
        return -1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
