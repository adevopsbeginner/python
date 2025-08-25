"""
1013. Partition Array Into Three Parts With Equal Sum
Easy
Topics
Companies
Hint
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])



Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104
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
    def leetcode(self, arr: List[int]) -> bool:
        sumarr = sum(arr)
        if sumarr % 3:
            return False
        sum1 = 0
        flag1 = 0
        sum2 = 0
        flag2 = 0
        flag3 = 0
        for each in arr:
            if flag1 == 0:
                sum1 += each
                if sum1 == sumarr//3:
                    flag1 = 1
            elif flag2 == 0:
                sum2 += each
                if sum2 == sumarr//3:
                    flag2 = 1
            else:
                flag3 = 1

        return flag1*flag2*flag3 > 0


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
