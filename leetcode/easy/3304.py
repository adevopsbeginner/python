"""
3304. Find the K-th Character in String Game I
Easy
Topics
premium lock icon
Companies
Hint
Alice and Bob are playing a game. Initially, Alice has a string word = "a".

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:

Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

 

Example 1:

Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd".
Example 2:

Input: k = 10

Output: "c"

 

Constraints:

1 <= k <= 500
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
    def leetcode(self, k: int) -> str:
        next = 0
        result = "a"
        for ii in range(11):
            ii2 = 2**ii
            if k <= ii2:
                k -= 1
                jj = ii
                while k > 0:
                    #print(k,jj,next)
                    jj -= 1
                    if k >= 2**jj:
                        k -= 2**jj
                        next += 1
                result = chr(ord("a")+next)
                break
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
