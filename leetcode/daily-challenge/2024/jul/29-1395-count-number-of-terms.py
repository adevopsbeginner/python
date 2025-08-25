"""

Code
Testcase
Testcase
Test Result
1395. Count Number of Teams
Attempted
Medium
Topics
Companies
Hint
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
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
    def leetcode(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for j in range(1, n-1):
            left_less = left_greater = right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j+1, n):
                if rating[k] > rating[j]:
                    right_greater += 1
                if rating[k] < rating[j]:
                    right_less += 1

            count += left_less * right_greater + left_greater * right_less

        return count

        ### time exceeded
        result = 0
        ll = len(rating)
        for ii in range(ll-2):
            for jj in range(ii+1,ll-1):
                if rating[ii] < rating[jj]:
                    for kk in range(jj+1,ll):
                        if rating[jj] < rating[kk]:
                            result += 1

                if rating[ii] > rating[jj]:
                    for kk in range(jj+1,ll):
                        if rating[jj] > rating[kk]:
                            result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
