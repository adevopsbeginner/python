'''
121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, prices: List[int]) -> int:
        ll = len(prices)
    
        ## 741ms Beats 64.00% of users with Python3
        buy  = ibuy  = prices[0]
        sell = isell = -1
        for ii in range(1,ll):
            if prices[ii] > ibuy:
                isell = max(isell, prices[ii])
                if isell-ibuy > sell-buy:
                    buy  = ibuy
                    sell = isell
            elif prices[ii] == ibuy:
                continue
            elif isell == -1:
                ibuy = prices[ii]
                continue
            else:
                ibuy  = prices[ii]
                isell = -1

        if sell == -1:
            return 0

        return sell-buy

        ## 208 / 212 testcases passed, time limit exceeded
        result = 0
        minp = min(prices)
        maxp = max(prices)
        for ii in range(ll-1):
            maxp = max(prices[ii:])
            if prices[ii] == maxp:
                continue
            else:
                result = max(result,maxp-prices[ii])

            if prices[ii] == minp:
                break

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,2,2,3,4,4,3]
    print(app.leetcode(a))
