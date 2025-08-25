"""
Q2. Maximum Number of Subsequences After One Inserting
Medium
5 pt.
You are given a string s consisting of uppercase English letters.

You are allowed to insert at most one uppercase English letter at any position (including the beginning or end) of the string.

Return the maximum number of "LCT" subsequences that can be formed in the resulting string after at most one insertion.

A subsequence is a non-empty string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "LMCT"

Output: 2

Explanation:

We can insert a "L" at the beginning of the string s to make "LLMCT", which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].

Example 2:

Input: s = "LCCT"

Output: 4

Explanation:

We can insert a "L" at the beginning of the string s to make "LLCCT", which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].

Example 3:

Input: s = "L"

Output: 0

Explanation:

Since it is not possible to obtain the subsequence "LCT" by inserting a single letter, the result is 0.

 

Constraints:

1 <= s.length <= 105
s consists of uppercase English letters.©leetcode
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str) -> int:
        add_none = 0
        add_l = 0
        add_c = 0
        add_t = 0
        ll = len(s)

        ### counting T
        total_t = 0
        for ii in range(ll):
            if s[ii] not in "LCT":
                continue
            elif s[ii] == "T":
                total_t += 1

        ### count L, LC, LCT
        add_none_count_l = 0
        add_none_count_lc = 0
        add_none_count_lct = 0
        
        add_l_count_l = 1 ### add L at the beginner
        add_l_count_lc = 0
        add_l_count_lct = 0

        add_none_count_t = 0
        max_l_times_t = 0
        for ii in range(ll):
            if s[ii] not in "LCT":
                continue

            if s[ii] == "L":
                add_none_count_l += 1
                add_l_count_l += 1
            if s[ii] == "C":
                add_none_count_lc += add_none_count_l
                add_l_count_lc += add_l_count_l
            if s[ii] == "T":
                add_none_count_t += 1
                add_none_count_lct += add_none_count_lc
                add_l_count_lct += add_l_count_lc

            max_l_times_t = max(max_l_times_t, add_none_count_l*(total_t-add_none_count_t))

        ### add T at the end
        add_t_count_lct = add_none_count_lct+add_none_count_lc

        return max(add_l_count_lct, add_none_count_lct+max_l_times_t, add_t_count_lct)

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
