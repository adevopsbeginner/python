"""
837. New 21 Game
Medium
Topics
premium lock icon
Companies
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
 

Constraints:

0 <= k <= n <= 104
1 <= maxPts <= 104
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
    def leetcode(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1
        if n >= k+maxPts:
            return 1
            
        dp = [0.0]*(n+1)
        dp[0] = 1
        pre_sum = 0
        for ii in range(1, n+1):
            #print(ii,dp,pre_sum)
            if ii-1 < k:
                pre_sum += dp[ii-1]
            if ii-maxPts-1 >= 0:
                pre_sum -= dp[ii-maxPts-1]
            dp[ii] += pre_sum/maxPts

        #print(dp)
            
        return sum(dp[k:n+1])


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
