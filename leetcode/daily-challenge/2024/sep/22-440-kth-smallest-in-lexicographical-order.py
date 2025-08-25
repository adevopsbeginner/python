"""
440. K-th Smallest in Lexicographical Order
Hard
Topics
Companies
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].



Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1


Constraints:

1 <= k <= n <= 109
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
    def leetcode(self, n: int, k: int) -> int:
        ### chatgpt
        #def find_kth_number(n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int) -> int:
            """Count how many numbers <= n start with the given prefix."""
            current = prefix
            next_prefix = prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1  # Start from the first number, so we reduce k by 1

        while k > 0:
            count = count_prefix(current, n)
            if count <= k:
                # If the k-th number is not in this prefix subtree, skip it
                k -= count
                current += 1  # Move to the next prefix
            else:
                # Go deeper in the current prefix subtree
                k -= 1  # Move to the next number in this subtree
                current *= 10  # Go deeper (lexicographically next)

        return current


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
