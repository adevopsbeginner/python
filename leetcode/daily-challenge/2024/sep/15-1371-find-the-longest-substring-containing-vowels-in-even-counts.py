"""
1371. Find the Longest Substring Containing Vowels in Even Counts
Solved
Medium
Topics
Companies
Hint
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.



Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.
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
    def leetcode(self, s: str) -> int:
        ### chatgpt
        # Map vowel to corresponding bit positions: a, e, i, o, u -> 0, 1, 2, 3, 4
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        # Current bitmask (start with 0 meaning all vowels have even count)
        current_mask = 0

        # Dictionary to store the first occurrence of each mask
        mask_to_index = {0: -1}

        max_length = 0
        for i, char in enumerate(s):
            # If the character is a vowel, flip the corresponding bit in the mask
            if char in vowel_to_bit:
                bit_position = vowel_to_bit[char]
                current_mask ^= (1 << bit_position)

            # If this mask has been seen before, calculate the length of the substring
            if current_mask in mask_to_index:
                max_length = max(max_length, i - mask_to_index[current_mask])
            else:
                # Store the first occurrence of this mask
                mask_to_index[current_mask] = i

        return max_length


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
