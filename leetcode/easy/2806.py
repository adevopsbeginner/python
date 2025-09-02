"""
2806. Account Balance After Rounded Purchase
Easy
Topics
premium lock icon
Companies
Hint
Initially, you have a bank account balance of 100 dollars.

You are given an integer purchaseAmount representing the amount you will spend on a purchase in dollars, in other words, its price.

When making the purchase, first the purchaseAmount is rounded to the nearest multiple of 10. Let us call this value roundedAmount. Then, roundedAmount dollars are removed from your bank account.

Return an integer denoting your final bank account balance after this purchase.

Notes:

0 is considered to be a multiple of 10 in this problem.
When rounding, 5 is rounded upward (5 is rounded to 10, 15 is rounded to 20, 25 to 30, and so on).
 

Example 1:

Input: purchaseAmount = 9

Output: 90

Explanation:

The nearest multiple of 10 to 9 is 10. So your account balance becomes 100 - 10 = 90.

Example 2:

Input: purchaseAmount = 15

Output: 80

Explanation:

The nearest multiple of 10 to 15 is 20. So your account balance becomes 100 - 20 = 80.

Example 3:

Input: purchaseAmount = 10
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
    def leetcode(self, purchaseAmount: int) -> int:
        purchaseAmount = (purchaseAmount+5)-(purchaseAmount+5)%10
        result = 100-purchaseAmount
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
