"""
2094. Finding 3-Digit Even Numbers

You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

 

Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array. 
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits. 
In this example, the digit 8 is used twice each time in 288, 828, and 882. 
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.
 

Constraints:

3 <= digits.length <= 100
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
    def leetcode(self, digits: List[int]) -> List[int]:
        result = []
        dd = defaultdict(int)
        for each in digits:
            dd[each] += 1
        ll = len(digits)
        for ii in range(ll):
            if digits[ii] == 0:
                continue
            for jj in range(ll):
                if jj == ii:
                    continue
                iijj = digits[ii]*100 + digits[jj]*10
                for each in [2,4,6,8,0]:
                    counti = 0
                    countj = 0
                    if digits[ii] == each:
                        counti = 1
                    if digits[jj] == each:
                        countj = 1
                    if dd[each]-counti-countj > 0:
                        iijjkk = iijj+each
                        if iijjkk not in result:
                            result.append(iijjkk)

        result.sort()
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
