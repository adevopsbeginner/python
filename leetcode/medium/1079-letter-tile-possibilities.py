"""
1079. Letter Tile Possibilities
Solved
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ll = len(tiles)
        dd = defaultdict(int)
        for each in tiles:
            dd[each] += 1
        
        ### 3rd try, chatgpt
        def backtrack(dd: dict):
            total = 0
            for each in dd:
                if dd[each] > 0:
                    dd[each] -= 1
                    total += 1+backtrack(dd)
                    dd[each] += 1
            return total
        
        return backtrack(dd)

        
        ### solution.2
        for ii in range(1,ll):
            ddkeys = list(dd.keys())
            lls = len(ddkeys)
            #print(ii,lls,ddkeys)
            for tile in tiles:    
                for jj in range(lls):
                    #print(ii,tile,jj,ddkeys[jj])
                    if dd[tile] == 1:
                        if tile in ddkeys[jj]:
                            continue
                    ddcount = defaultdict(int)
                    for c in ddkeys[jj]:
                        ddcount[c] += 1
                    if ddcount[tile] < dd[tile]:
                        dd[ddkeys[jj]+tile] += 1

        result = len(dd.keys())
        #print(dd.keys)
        for each in dd:
            ddcount = defaultdict(int)
            for c in each:
                ddcount[c] += 1
            for c in dd:
                if ddcount[c] > dd[c]:
                    result -= 1
                    break

        return result

        ### solution.1, 0x11..11
        for ii in range(1, 256):
            #s= 
            if s not in sequences:
                sequences.append(s)
                result += 1
        return result