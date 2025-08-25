"""
1089. Duplicate Zeros
Easy
Topics
Companies
Hint
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
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
    def leetcode(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ll = len(arr)
        countl = 0
        index_front = 0
        index_end = ll-1
        while index_front < ll:
            if arr[index_front] == 0:
                countl += 2
            else:
                countl += 1

            if countl >= ll:
                if countl == ll+1:
                    arr[-1] = 0
                    index_end -= 1
                    index_front -= 1 
                break
            index_front += 1
        #print(1, index_front, index_end)

        while index_front >= 0:
            #print(2, index_front, index_end)
            if arr[index_front] == 0:
                arr[index_end] = 0
                index_end -= 1
                arr[index_end] = 0
            else:
                arr[index_end] = arr[index_front]
            index_end -= 1
            index_front -= 1


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
