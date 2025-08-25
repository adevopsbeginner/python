"""

Code
Testcase
Test Result
Test Result
Q2. Maximize Score of Numbers in Ranges
Medium
5 pt.
You are given an array of integers start and an integer d, representing n intervals [start[i], start[i] + d].

You are asked to choose n integers where the ith integer must belong to the ith interval. The score of the chosen integers is defined as the minimum absolute difference between any two integers that have been chosen.

Return the maximum possible score of the chosen integers.



Example 1:

Input: start = [6,0,3], d = 2

Output: 4

Explanation:

The maximum possible score can be obtained by choosing integers: 8, 0, and 4. The score of these chosen integers is min(|8 - 0|, |8 - 4|, |0 - 4|) which equals 4.

Example 2:

Input: start = [2,6,13,13], d = 5

Output: 5

Explanation:

The maximum possible score can be obtained by choosing integers: 2, 7, 13, and 18. The score of these chosen integers is min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|) which equals 5.



Constraints:

2 <= start.length <= 105
0 <= start[i] <= 109
0 <= d <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, start: List[int], d: int) -> int:
        ### answer
        start.sort()
        l, r = 0, 2 * 10 ** 9
        while (l <= r):
            m = (l + r) // 2
            x = start[0]
            flg = True
            for i in range(1, len(start)):
                x += m
                if x < start[i]: x = start[i]
                if x > start[i] + d:
                    flg = False
                    break
            if flg:
                l = m + 1
            else:
                r = m - 1
        return r
        ### time exceeded (ll), or wrong answer(loop 100 times)
        ll = len(start)
        start.sort()
        result = (start[-1]+d-start[0])//(ll-1)
        # for ii in range(1,20):
        #     for jj in range(ii,ll):
        #         result = min(result,(abs(start[jj]+d-start[jj-ii]))//ii)
        for ii in range(1,ll):
            for jj in range(ii,ll):
                result = min(result,(start[jj]+d-start[jj-ii])//ii)

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
