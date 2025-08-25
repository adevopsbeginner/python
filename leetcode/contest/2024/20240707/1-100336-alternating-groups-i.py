"""
100336. Alternating Groups I
User Accepted:13626
User Tried:15239
Total Accepted:13871
Total Submissions:19085
Difficulty:Easy
There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.



Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:



Alternating groups:





Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, colors: List[int]) -> int:
        ll = len(colors)
        result = 0
        if colors[0] != colors[-1]:
            if colors[0] != colors[1]:
                result += 1
            if colors[-2] != colors[-1]:
                result += 1

        for ii in range(1,ll-1):
            if colors[ii] != colors[ii-1] and colors[ii] != colors[ii+1]:
                print(result,ii)
                result += 1

        return result

if __name__ == "__main__":
    app = Solution()
    a = [0,1,0,0,1]
    b = 2
    print(app.leetcode(a))
