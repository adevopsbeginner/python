"""
2231. Largest Number After Digit Swaps by Parity
Easy
Topics
Companies
Hint
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

 

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
 

Constraints:

1 <= num <= 109
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
    def leetcode(self, num: int) -> int:
        ll = 0
        copy = num
        odd = []
        even = []
        parity = []
        while copy:
            digit = copy%10
            if digit%2 > 0:
                odd.append(digit)
                parity.append(1)
            else:
                even.append(digit)
                parity.append(0)
            copy //= 10
            ll += 1
        odd.sort()
        even.sort()
        result = 0
        while len(parity):
            if parity.pop() == 0:
                result = result*10 + even.pop()
            else:
                result = result*10 + odd.pop()

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
