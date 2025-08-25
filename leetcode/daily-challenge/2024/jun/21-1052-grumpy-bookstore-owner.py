"""
1052. Grumpy Bookstore Owner
Medium
Topics
Companies
Hint
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1


Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
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
    def leetcode(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = 0
        n = len(customers)
        for ii in range(n):
            if grumpy[ii] == 0:
                total += customers[ii]

        result = total

        for ii in range(n-minutes+1):
            iisatisfy = 0
            for jj in range(minutes):
                iisatisfy += customers[ii+jj]*grumpy[ii+jj]
            result = max(result, total+iisatisfy)
        return result

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    a = [0,2,2]
    #a = [3,2,1,2,1,7]
    b = [5]
    k = 2
    w = 0
    profits = [1,2,3]
    capital = [0,1,2]
    print(app.leetcode(k,w,profits,capital))
