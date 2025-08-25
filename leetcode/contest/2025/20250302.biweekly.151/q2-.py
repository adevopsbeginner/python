"""
Q2. Find the Number of Copy Arrays
Medium
4 pt.
You are given an array original of length n and a 2D array bounds of length n x 2, where bounds[i] = [ui, vi].

You need to find the number of possible arrays copy of length n such that:

(copy[i] - copy[i - 1]) == (original[i] - original[i - 1]) for 1 <= i <= n - 1.
ui <= copy[i] <= vi for 0 <= i <= n - 1.
Return the number of such arrays.

 

Example 1:

Input: original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]

Output: 2

Explanation:

The possible arrays are:

[1, 2, 3, 4]
[2, 3, 4, 5]
Example 2:

Input: original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]

Output: 4

Explanation:

The possible arrays are:

[1, 2, 3, 4]
[2, 3, 4, 5]
[3, 4, 5, 6]
[4, 5, 6, 7]
Example 3:

Input: original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]

Output: 0

Explanation:

No array is possible.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, original: List[int], bounds: List[List[int]]) -> int:
        ll = len(original)
        low, high = bounds[0]

        for ii in range(1,ll):
            diff = original[ii] - original[ii-1]
            low, high = low+diff, high+diff
            u, v = bounds[ii]
            low = max(low, u)
            high = min(high, v)
            if low > high:
                return 0
        return high - low + 1

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
