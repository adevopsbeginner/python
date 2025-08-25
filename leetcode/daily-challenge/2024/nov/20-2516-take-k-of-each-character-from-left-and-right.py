"""
2516. Take K of Each Character From Left and Right
Medium
Topics
Companies
Hint
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
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
    def leetcode(self, s: str, k: int) -> int:
        ll = len(s)
        if k == 0:
            return 0

        na = nb = nc = 0
        for each in s:
            if each == "a":
                na += 1
            elif each == "b":
                nb += 1
            else:
                nc += 1
        if min(na,nb,nc) < k:
            return -1

        front = 0
        na = nb = nc = 0
        while front < ll:
            each = s[front]
            if each == "a":
                na += 1
            elif each == "b":
                nb += 1
            else:
                nc += 1
            
            if min(na,nb,nc) == k:
                break
            front += 1

        result = front+1
        na_backward = nb_backward = nc_backward = 0
        for ii in range(ll):
            each = s[ll-1-ii]
            #print(result,na,na_backward,nb,nb_backward,nc, nc_backward,each,ii)
            if each == "a":
                na_backward += 1
            elif each == "b":
                nb_backward += 1
            else:
                nc_backward += 1
            #print(result,na,na_backward,nb,nb_backward,nc, nc_backward)
            while na+na_backward >= k and nb+nb_backward >= k and nc+nc_backward >= k and front >= 0:
                #print(result,na,na_backward,nb,nb_backward,nc, nc_backward,front,s[front],ii,s[ll-1-ii])
                if na+na_backward > k and s[front] == "a":
                    front -= 1
                    na -= 1
                elif nb+nb_backward > k and s[front] == "b":
                    front -= 1
                    nb -= 1
                elif nc+nc_backward > k and s[front] == "c":
                    front -= 1
                    nc -= 1
                else:
                    break
            if result > (front+1) + (ii+1):
                result = (front+1) + (ii+1)
            if front <= 0:
                break

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
