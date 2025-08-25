"""
873. Length of Longest Fibonacci Subsequence
Solved
Medium
Topics
Companies
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
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
    def leetcode(self, arr: List[int]) -> int:
        ll = len(arr)
        dd = defaultdict()
        for ii in range(ll):
            dd[arr[ii]] = ii
        
        dp = defaultdict(lambda: 2)
        result = 0
        for i3 in range(ll):
            for i2 in range(i3):
                if arr[i3]-arr[i2] in dd:
                    i1 = dd[arr[i3]-arr[i2]]
                    if i1 < i2:
                        dp[i2, i3] = dp[i1, i2] + 1
                        result = max(result, dp[i2, i3])
        if result < 3:
            return 0
        return result

        ### wrong answer
        ll = len(arr)
        q = []
        for ii in range(ll-2):
            for jj in range(ii+1,ll-1):
                if arr[ii] + arr[jj] > arr[-1]:
                    continue
                if arr[ii] + arr[jj] in arr:
                    q.append([arr[ii], arr[jj], arr[ii] + arr[jj]])
        llq = len(q)
        for ii in range(ll):
            for jj in range(llq):
                #print(ii, arr[ii], jj, q[jj])
                # if arr[ii] <= q[jj][-1]:
                #     continue
                if arr[ii] == q[jj][-1] + q[jj][-2]:
                    q[jj].append(arr[ii])
                    break
        
        #print(q)
        result = 0
        if len(q):
            result = len(max(q, key=lambda x:len(x)))

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
