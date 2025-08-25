"""
100301. Count Pairs That Form a Complete Day II
User Accepted:11934
User Tried:16372
Total Accepted:12260
Total Submissions:28969
Difficulty:Medium
Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where i < j and hours[i] + hours[j] forms a complete day.

A complete day is defined as a time duration that is an exact multiple of 24 hours.

For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.



Example 1:

Input: hours = [12,12,30,24,24]

Output: 2

Explanation: The pairs of indices that form a complete day are (0, 1) and (3, 4).

Example 2:

Input: hours = [72,48,24,3]

Output: 3

Explanation: The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).



Constraints:

1 <= hours.length <= 5 * 105
1 <= hours[i] <= 109
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, hours: List[int]) -> int:
        ll = len(hours)
        result = 0
        dd = defaultdict(int)

        for ii in range(ll):
            hours[ii] %= 24
            if hours[ii] < 0:
                hours[ii] += 24

        for each in hours:
            dd[each] += 1

        # for each in dd:
        #     print(each,dd[each])

        for each in dd:
            if each == 0 or each == 12:
                pass
            elif 24 - each in dd:
                print(each, dd[each])
                result += dd[each] * dd[24 - each]

        # print(result)
        result //= 2
        if dd[0] > 1:
            result += dd[0] * (dd[0] - 1) // 2
        if dd[12] > 1:
            result += dd[12] * (dd[12] - 1) // 2

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
