"""

Code
Testcase
Test Result
Test Result
1122. Relative Sort Array
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
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dd1 = {}
        dd2 = {}
        ll1 = len(arr1)
        ll2 = len(arr2)
        result = []
        notinlist = []
        for ii in range(ll1):
            if arr1[ii] not in arr2:
                notinlist.append(arr1[ii])
            elif arr1[ii] in dd1:
                dd1[arr1[ii]] += 1
            else:
                dd1[arr1[ii]] = 1

        for k,v in dd1.items():
            print(k,v)

        for ii in range(ll2):
            result += [arr2[ii]]*dd1[arr2[ii]]
            dd1[arr2[ii]] = 0

        result += sorted(notinlist)
        return result

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,-2,-3,1]
    b = [5]
    k = 5
    print(app.leetcode(a,b))
