"""
122. Best Time to Buy and Sell Stock II
Solved
Medium
Topics
Companies
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
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
    def leetcode(self, prices: List[int]) -> int:
        ll = len(prices)
        if max(prices) == min(prices):
            return 0
        high = []
        low = []
        
        ### for p[ii] == p[ii-1]
        bigger_than_left = 0
        smaller_than_left = 0
        for ii in range(1,ll):
            if prices[ii] > prices[ii-1]:
                if smaller_than_left > 0:
                    low.append(prices[ii-1])
                    smaller_than_left = 0
                bigger_than_left = 1
            elif prices[ii] < prices[ii-1]:
                if bigger_than_left > 0:
                    if len(low) == 0:
                        low = [prices[0]]
                    high.append(prices[ii-1])
                    bigger_than_left = 0
                smaller_than_left = 1
        ### for the end of array
        if smaller_than_left > 0:
            low.append(prices[-1])
        if bigger_than_left > 0:
            if len(low) == 0:
                low = [prices[0]]
            high.append(prices[-1])

        #print(low, high)

        result = 0
        for ii in range(min(len(low), len(high))):
            result += high[ii]-low[ii]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
