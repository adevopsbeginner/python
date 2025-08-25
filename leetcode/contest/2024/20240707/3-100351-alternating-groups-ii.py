"""
100351. Alternating Groups II
User Accepted:286
User Tried:744
Total Accepted:289
Total Submissions:1026
Difficulty:Medium
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.



Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:





Constraints:

3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, colors: List[int], k: int) -> int:
        ll = len(colors)
        result = 0
        lc = [0] * ll
        for ii in range(ll-1):
            lc[ii] = colors[ii]^colors[ii+1]
        lc[-1] = colors[-1]^colors[0]
        print(lc)
        sumlc = sum(lc)
        if sumlc == ll:
            return ll
        for ii in range(ll):
            if lc[ii] == 0:
                start = (ii+1)%ll
                break
        ilast = start
        for ii in range(ll):
            current = (start+ii)
            print(ii,start,current)
            if lc[current % ll] == 0:
                # print(ilast,ii,current)
                result += max(current-ilast+1-k+1, 0)
                print(100,result,current,ilast)
                ilast = current

            # else:
            #     print(ii,lc[current % ll])
        return result


        ## time limit exceeded
        ll = len(colors)
        result = 0
        ii = 0
        while ii < ll:
            flagadd = 1
            for jj in range(1,k-1):
                if colors[(ii+jj)%ll] == colors[(ii+jj-1)%ll] or colors[(ii+jj)%ll] == colors[(ii+jj+1)%ll]:
                    flagadd = 0
                    break
            if flagadd:
                result += 1
                ii += 1
            else:
                ii += jj

        return result

if __name__ == "__main__":
    app = Solution()
    a = [0,1,0,1,0]
    k = 3
    a = [0,1,0,0,1,0,1]
    k = 6
    a = [0,0,0,1]
    k = 3
    print(app.leetcode(a,k))
