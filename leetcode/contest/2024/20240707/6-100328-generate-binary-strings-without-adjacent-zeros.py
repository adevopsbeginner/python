"""
100328. Generate Binary Strings Without Adjacent Zeros
Medium
You are given a positive integer n.

A binary string x is valid if all
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.



Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".



Constraints:

1 <= n <= 18
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> List[str]:
        result = ["1","0"]
        for ii in range(1,n):
            ll = len(result)
            currnt = []
            for ii in range(ll):
                if result[ii][-1] == "0":
                    currnt.append(result[ii]+"1")
                else:
                    currnt.append(result[ii]+"0")
                    currnt.append(result[ii]+"1")
            result = currnt
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
