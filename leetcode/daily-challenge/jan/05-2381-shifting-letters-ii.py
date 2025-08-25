"""
2381. Shifting Letters II
Attempted
Medium
Topics
Companies
Hint
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 

Constraints:

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, s: str, shifts: List[List[int]]) -> str:
        ### chatgpt
        n = len(s)
        shift_accum = [0] * (n + 1)
        
        # Record shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift_accum[start] += 1
                shift_accum[end + 1] -= 1
            else:
                shift_accum[start] -= 1
                shift_accum[end + 1] += 1
        
        # Compute cumulative shifts
        for i in range(1, n):
            shift_accum[i] += shift_accum[i - 1]
        
        # Apply shifts to the string
        result = []
        for i in range(n):
            effective_shift = shift_accum[i] % 26
            new_char = chr((ord(s[i]) - ord('a') + effective_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

        ### time limit exceeded
        ll = len(s)
        ls = list(s)
        #print(ls)
        for start,end,direction in shifts:
            for ii in range(start,end+1):
                if direction == 0:
                    ls[ii] = chr((ord(ls[ii])-ord("a")+26-1)%26+ord("a"))
                else:
                    ls[ii] = chr((ord(ls[ii])-ord("a")+1)%26+ord("a"))

        return "".join(ls)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
