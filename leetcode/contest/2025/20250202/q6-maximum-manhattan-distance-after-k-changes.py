"""
Q2. Maximum Manhattan Distance After K Changes
Medium
4 pt.
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

'N' : Move north by 1 unit.
'S' : Move south by 1 unit.
'E' : Move east by 1 unit.
'W' : Move west by 1 unit.
Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
 

Example 1:

Input: s = "NWSE", k = 1

Output: 3

Explanation:

Change s[2] from 'S' to 'N'. The string s becomes "NWNE".

Movement	Position (x, y)	Manhattan Distance	Maximum
s[0] == 'N'	(0, 1)	0 + 1 = 1	1
s[1] == 'W'	(-1, 1)	1 + 1 = 2	2
s[2] == 'N'	(-1, 2)	1 + 2 = 3	3
s[3] == 'E'	(0, 2)	0 + 2 = 2	3
The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.

Example 2:

Input: s = "NSWWEW", k = 3

Output: 6

Explanation:

Change s[1] from 'S' to 'N', and s[4] from 'E' to 'W'. The string s becomes "NNWWWW".

The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.

 

Constraints:

1 <= s.length <= 105
0 <= k <= s.length
s consists of only 'N', 'S', 'E', and 'W'.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str, k: int) -> int:
        nwse = [0,0,0,0]
        result = 0
        ll = len(s)
        for ii in range(ll):
            if s[ii] == "N":
                nwse[0] += 1
            elif s[ii] == "W":
                nwse[1] += 1
            elif s[ii] == "S":
                nwse[2] += 1
            elif s[ii] == "E":
                nwse[3] += 1
            minns = min(nwse[0],nwse[2])
            minew = min(nwse[1],nwse[3])
            maxns = max(nwse[0],nwse[2])
            maxew = max(nwse[1],nwse[3])
            manhattan = maxns-minns + maxew-minew + min(k,minns+minew)*2
            #print(ii,nwse,manhattan, result)
            result = max(result, manhattan)
            
        return result©leetcode

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
