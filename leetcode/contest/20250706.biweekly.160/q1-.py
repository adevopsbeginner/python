"""
Q1. Hexadecimal and Hexatrigesimal Conversion
Easy
3 pt.
You are given an integer n.

Return the concatenation of the hexadecimal representation of n2 and the hexatrigesimal representation of n3.

A hexadecimal number is defined as a base-16 numeral system that uses the digits 0 – 9 and the uppercase letters A - F to represent values from 0 to 15.

A hexatrigesimal number is defined as a base-36 numeral system that uses the digits 0 – 9 and the uppercase letters A - Z to represent values from 0 to 35.

 

Example 1:

Input: n = 13

Output: "A91P1"

Explanation:

n2 = 13 * 13 = 169. In hexadecimal, it converts to (10 * 16) + 9 = 169, which corresponds to "A9".
n3 = 13 * 13 * 13 = 2197. In hexatrigesimal, it converts to (1 * 362) + (25 * 36) + 1 = 2197, which corresponds to "1P1".
Concatenating both results gives "A9" + "1P1" = "A91P1".
Example 2:

Input: n = 36

Output: "5101000"

Explanation:

n2 = 36 * 36 = 1296. In hexadecimal, it converts to (5 * 162) + (1 * 16) + 0 = 1296, which corresponds to "510".
n3 = 36 * 36 * 36 = 46656. In hexatrigesimal, it converts to (1 * 363) + (0 * 362) + (0 * 36) + 0 = 46656, which corresponds to "1000".
Concatenating both results gives "510" + "1000" = "5101000".
 

Constraints:

1 <= n <= 1000©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> str:
        n2 = n*n
        n3 = n*n2
        result = ""
        while n3 > 0:
            nn = n3%36
            if nn < 10:
                result = str(nn)+result
            else:
                result = chr(ord("A")+nn-10)+result
            n3 //= 36

        while n2 > 0:
            nn = n2%16
            if nn < 10:
                result = str(nn)+result
            else:
                result = chr(ord("A")+nn-10)+result
            n2 //= 16

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
