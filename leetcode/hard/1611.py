"""
1611. Minimum One Bit Operations to Make Integers Zero
Hard
Topics
￼
Companies
Hint
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
 

Constraints:

0 <= n <= 109
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, n: int) -> int:
        nn = [0, 1, 3, 2, 7, 6, 4, 5]
        if n < len(nn):
            return nn[n]
        
        for ii in range(31, -1, -1):
            if ii == 0:
                return 1
            if ii == 1:
                if n == 2:
                    return 3
                if n == 3:
                    return 2

            high1 = 1<<ii
            high2 = 1<<(ii-1)
            #print(ii, high1, high2, high1^high2^n)
            if n & high1 > 0:
                #print(high1, high2, high1^high2^n)
                if n & high2 > 0:
                    ### 1 to B, adding C
                    return self.minimumOneBitOperations(high2) + 1 + self.minimumOneBitOperations(high1^high2^n)
                else:
                    ### 1 to B, adding B minus C
                    return self.minimumOneBitOperations(high2)*2 + 1 - self.minimumOneBitOperations(high1^n)

        return 0
