"""
2554. Maximum Number of Integers to Choose From a Range I
Attempted
Medium
Topics
Companies
Hint
You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.

 

Example 1:

Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: You can choose the integers 2 and 4.
2 and 4 are from the range [1, 5], both did not appear in banned, and their sum is 6, which did not exceed maxSum.
Example 2:

Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: You cannot choose any integer while following the mentioned conditions.
Example 3:

Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: You can choose the integers 1, 2, 3, 4, 5, 6, and 7.
They are from the range [1, 7], all did not appear in banned, and their sum is 28, which did not exceed maxSum.
 

Constraints:

1 <= banned.length <= 104
1 <= banned[i], n <= 104
1 <= maxSum <= 109
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
    def leetcode(self, banned: List[int], n: int, maxSum: int) -> int:
        ll = len(banned)
        banned.sort()
        result = 0
        total = 0
        banned.append(n+1)
        banned.append(0)
        #print(banned)
        for ii in range(ll+1):
            if banned[ii] == banned[ii-1]:
                continue
            if banned[ii] == banned[ii-1]+1:
                continue
            for jj in range(banned[ii-1]+1,min(banned[ii],n+1)):
                if total + jj <= maxSum:
                    total += jj
                    result += 1
                    # if result > 200:
                    #     print(ii, jj, result,total,banned[ii-1], banned[ii])

            if banned[ii] >= n:
                break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
