"""

Code
Testcase
Test Result
Test Result
728. Self Dividing Numbers
Easy
Topics
Companies
Hint
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].



Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]


Constraints:

1 <= left <= right <= 104
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
    def leetcode(self, left: int, right: int) -> List[int]:
        result = []
        for ii in range(left,right+1):
            digits = [-1,-1,-1,-1]

            if ii < 10:
                result.append(ii)
                continue

            if ii >= 10000:
                continue

            if ii >= 1000:
                digit = ii//1000%10
                digits[0] = digit
                if 0 in digits:
                    continue
                if ii % digit:
                    continue

            if ii >= 100:
                digit = ii//100%10
                digits[1] = digit
                if 0 in digits:
                    continue
                if ii % digit:
                    continue

            if ii >= 10:
                digit = ii//10%10
                digits[2] = digit
                if 0 in digits:
                    continue
                if ii % digit:
                    continue

            if ii >= 1:
                digit = ii % 10
                digits[3] = digit
                if 0 in digits:
                    continue
                if ii % digit:
                    continue

            result.append(ii)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
