"""
1122. Relative Sort Array
Solved
Easy
Topics
Companies
Hint
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
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
    def leetcode(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ll1 = len(arr1)
        ll2 = len(arr2)
        not_in2 = []
        result = [0]*ll1
        dd = defaultdict(int)
        total = 0
        index = 0
        for each in arr1:
            if each in arr2:
                total += 1
                dd[each] += 1
            else:
                not_in2.append(each)
        index = 0
        for each in arr2:
            for ii in range(dd[each]):
                result[index] = each
                index += 1
        not_in2.sort()
        for each in not_in2:
            result[index] = each
            index += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
