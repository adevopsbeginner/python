"""
3258. Count Substrings That Satisfy K-Constraint I
Easy
Topics
premium lock icon
Companies
Hint
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of substrings of s that satisfy the k-constraint.

 

Example 1:

Input: s = "10101", k = 1

Output: 12

Explanation:

Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

Example 2:

Input: s = "1010101", k = 2

Output: 25

Explanation:

Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:

Input: s = "11111", k = 1

Output: 15

Explanation:

All substrings of s satisfy the k-constraint.

 

Constraints:

1 <= s.length <= 50 
1 <= k <= s.length
s[i] is either '0' or '1'.
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
    def leetcode(self, s: str, k: int) -> int:
        ll = len(s)
        result = 0
        for ii in range(ll):
            count0 = 0
            count1 = 0
            for jj in range(ii,ll):
                #print(ii,jj)
                if s[jj] == "1":
                    count1 += 1
                else:
                    count0 += 1

                if count0 > k and count1> k:
                    break
                result +=1
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
