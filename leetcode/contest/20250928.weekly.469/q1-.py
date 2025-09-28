"""
Q1. Compute Decimal Representation
Easy
3 pt.
You are given a positive integer n.

A positive integer is a base-10 component if it is the product of a single digit from 1 to 9 and a non-negative power of 10. For example, 500, 30, and 7 are base-10 components, while 537, 102, and 11 are not.

Express n as a sum of only base-10 components, using the fewest base-10 components possible.

Return an array containing these base-10 components in descending order.

 

Example 1:

Input: n = 537

Output: [500,30,7]

Explanation:

We can express 537 as 500 + 30 + 7. It is impossible to express 537 as a sum using fewer than 3 base-10 components.

Example 2:

Input: n = 102

Output: [100,2]

Explanation:

We can express 102 as 100 + 2. 102 is not a base-10 component, which means 2 base-10 components are needed.

Example 3:

Input: n = 6

Output: [6]

Explanation:

6 is a base-10 component.

 

Constraints:

1 <= n <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> List[int]:
        result = []
        for ii in range(10,-1,-1):
            digit = n//(10**ii)
            if digit != 0:
                result.append(digit*(10**ii))
                n %= digit*(10**ii)
                
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
