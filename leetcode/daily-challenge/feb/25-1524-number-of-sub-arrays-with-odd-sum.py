"""
1524. Number of Sub-arrays With Odd Sum
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
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
        result = 0
        ll = len(arr)
        for ii in range(ll):
            arr[ii] %= 2

        count = 0
        sum0 = 0
        for ii in range(ll):
            sum0 += arr[ii]
            count += sum0%2
        result += count

        for ii in range(1, ll):
            if count == 0:
                break
            if arr[ii-1] == 1:
                ### 10...
                if arr[ii] == 0:
                    count = ll-(ii-1)-count
                ### 01...
                else:
                    count = (ll-ii-1)-(count-1)+1
            result += count
            #print(ii, result, count)

        return result%(10**9+7)
        
        ### brute force, time limit exceeded
        for ii in range(ll):
            count = 0
            for jj in range(ii,ll):
                count += arr[jj]
                result += count%2

        return result%(10**9+7)

        ### wrong answer because this is about sub-arrays and we keep the same order
        result = 0
        ll = len(arr)
        count1 = 0
        for each in arr:
            count1 += each%2
        count0 = ll-count1
        for ii in range(count1):
            result += (count1-ii)//2
            if (count1-ii)%2 == 1:
                result += +1+count0

        return result%(10**9+7)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
