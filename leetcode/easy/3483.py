"""
3483. Unique 3-Digit Even Numbers
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.

Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

 

Constraints:

3 <= digits.length <= 10
0 <= digits[i] <= 9
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
    def leetcode(self, digits: List[int]) -> int:
        ll = len(digits)
        result = []
        for ii in range(ll):
            if digits[ii] == 0:
                continue
            for jj in range(ll):
                if jj == ii:
                    continue
                if digits[jj]%2 > 0:
                    continue
                for kk in range(ll):
                    if kk == ii:
                        continue
                    if kk == jj:
                        continue
                    if digits[ii]*100+digits[kk]*10+digits[jj] in result:
                        continue
                    result.append(digits[ii]*100+digits[kk]*10+digits[jj])
        #print(result)
        return len(result)
            
        ### wrong answer, we want unique numbers
        ll = len(digits)
        count2 = 0
        count0 = 0
        for digit in digits:
            if digit == 0:
                count0 += 1
            if digit%2 == 0:
                count2 += 1

        ### total number of 3 digits even number
        result = count2*(ll-1)*(ll-2)

        ### get rid of leading 0 ones
        result -= count0*(ll-2)*(count2-1)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
