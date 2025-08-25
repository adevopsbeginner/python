"""
Q1. Minimum Sensors to Cover Grid
Medium
4 pt.
You are given n × m grid and an integer k.

A sensor placed on cell (r, c) covers all cells whose Chebyshev distance from (r, c) is at most k.

The Chebyshev distance between two cells (r1, c1) and (r2, c2) is max(|r1 − r2|,|c1 − c2|).

Your task is to return the minimum number of sensors required to cover every cell of the grid.

 

Example 1:

Input: n = 5, m = 5, k = 1

Output: 4

Explanation:

Placing sensors at positions (0, 3), (1, 0), (3, 3), and (4, 1) ensures every cell in the grid is covered. Thus, the answer is 4.

Example 2:

Input: n = 2, m = 2, k = 2

Output: 1

Explanation:

With k = 2, a single sensor can cover the entire 2 * 2 grid regardless of its position. Thus, the answer is 1.

 

Constraints:

1 <= n <= 103
1 <= m <= 103
0 <= k <= 103©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int, m: int, k: int) -> int:
        kk = 1+k*2
        rr = n//kk
        if n%kk:
            rr += 1
        cc = m//kk
        if m%kk:
            cc += 1
        return rr*cc

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
