"""

Code
Testcase
Test Result
Test Result
1323. Maximum 69 Number
Easy
Topics
Companies
Hint
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.
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
        digits = []
        while num > 0:
            digits.append(num%10)
            num //= 10
        reversed_digits = digits[::-1]
        #print(reversed_digits)
        ll = len(digits)
        for ii in range(ll):
            if reversed_digits[ii] == 6:
                reversed_digits[ii] = 9
                break
        result = 0
        for ii in range(ll):
            result = result*10+reversed_digits[ii]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
