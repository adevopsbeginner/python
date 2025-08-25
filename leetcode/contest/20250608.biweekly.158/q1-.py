"""
Q1. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
Medium
4 pt.
You are given two integer arrays x and y, each of length n. You must choose three distinct indices i, j, and k such that:

x[i] != x[j]
x[j] != x[k]
x[k] != x[i]
Your goal is to maximize the value of y[i] + y[j] + y[k] under these conditions. Return the maximum possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

 

Example 1:

Input: x = [1,2,1,3,2], y = [5,3,4,6,2]

Output: 14

Explanation:

Choose i = 0 (x[i] = 1, y[i] = 5), j = 1 (x[j] = 2, y[j] = 3), k = 3 (x[k] = 3, y[k] = 6).
All three values chosen from x are distinct. 5 + 3 + 6 = 14 is the maximum we can obtain. Hence, the output is 14.
Example 2:

Input: x = [1,2,1,2], y = [4,5,6,7]

Output: -1

Explanation:

There are only two distinct values in x. Hence, the output is -1.
 

Constraints:

n == x.length == y.length
3 <= n <= 105
1 <= x[i], y[i] <= 106
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        for ii in range(n):
            y[ii] = [y[ii],ii]
        y.sort(reverse=True)
        result = y[0][0]
        i = j = k = y[0][1]
        for jj in range(1, n):
            if x[y[jj][1]] == x[i]:
                if jj == n-1:
                    return -1
                continue
            result += y[jj][0]
            j = y[jj][1]
            if jj == n-1:
                return -1
            #print(y, result, i,j,k)

            for kk in range(jj+1, n):
                if x[y[kk][1]] == x[i] or x[y[kk][1]] == x[j]:
                    if kk == n-1:
                        return -1
                    continue
                result += y[kk][0]
                k = y[kk][1]
                return result

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
