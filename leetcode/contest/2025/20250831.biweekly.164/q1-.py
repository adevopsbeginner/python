"""
Q1. Find The Least Frequent Digit
Easy
3 pt.
Given an integer n, find the digit that occurs least frequently in its decimal representation. If multiple digits have the same frequency, choose the smallest digit.

Return the chosen digit as an integer.

The frequency of a digit x is the number of times it appears in the decimal representation of n.
 

Example 1:

Input: n = 1553322

Output: 1

Explanation:

The least frequent digit in n is 1, which appears only once. All other digits appear twice.

Example 2:

Input: n = 723344511

Output: 2

Explanation:

The least frequent digits in n are 7, 2, and 5; each appears only once.

 

Constraints:

1 <= n <= 231​​​​​​​ - 1
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> int:
        listn = list(str(n))
        result = listn[0]
        dd = defaultdict(int)
        for each in listn:
            dd[each] += 1

        #print(dd)
        for num in "0123456789":
            if num in dd:
                #print(num, result, dd[num], dd[result])
                if dd[num] < dd[result]:
                    result = num
                elif dd[num] == dd[result]:
                    if int(num) < int(result):
                        result = num
            
        return int(result)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
