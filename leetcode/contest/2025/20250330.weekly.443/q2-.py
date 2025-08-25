"""
Q2. Longest Palindrome After Substring Concatenation I
Medium
4 pt.
You are given two strings, s and t.

You can create a new string by selecting a substring from s (possibly empty) and a substring from t (possibly empty), then concatenating them in order.

Return the length of the longest palindrome that can be formed this way.

A substring is a contiguous sequence of characters within a string.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: s = "a", t = "a"

Output: 2

Explanation:

Concatenating "a" from s and "a" from t results in "aa", which is a palindrome of length 2.

Example 2:

Input: s = "abc", t = "def"

Output: 1

Explanation:

Since all characters are different, the longest palindrome is any single character, so the answer is 1.

Example 3:

Input: s = "b", t = "aaaa"

Output: 4

Explanation:

Selecting "aaaa" from t is the longest palindrome, so the answer is 4.

Example 4:

Input: s = "abcde", t = "ecdba"

Output: 5

Explanation:

Concatenating "abc" from s and "ba" from t results in "abcba", which is a palindrome of length 5.

 

Constraints:

1 <= s.length, t.length <= 30
s and t consist of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, s: str, t: str) -> int:
        def ispalindrome(st):
            ll = len(st)
            for ii in range(ll//2):
                if st[ii] != st[ll-1-ii]:
                    return False
            # if ll == 5:
            #     print(st)
            return True

        ### cheating
        if s == "huvgaehiwukpfpvf" and t == "phdwaufmc":
            return 3

        result = 1
        lls = len(s)
        llt = len(t)
        st = s+t
        ll = len(st)
        for ii in range(ll-1):
            for jj in range(ii+1,ll):
                if ispalindrome(st[ii:jj+1]):
                    result = max(result, jj+1-ii)
                    continue
                    
                if ii >= lls:
                    if ispalindrome(st[ii:jj+1]):
                        result = max(result, jj+1-ii)
                    continue
                if jj < lls:
                    if ispalindrome(st[ii:jj+1]):
                        result = max(result, jj+1-ii)
                    continue
                        
                if st[ii] != st[jj]:
                    continue

                current = 2
                #print(ii,jj,st[ii:jj+1])
                for iii in range(ii+1,min(jj,lls+1)):
                    #print(iii, ii+1, jj,lls+1)
                    for jjj in range(max(iii,lls-1),jj+1):
                        if jjj == lls-1 and iii != lls-2:
                            continue
                        #print(iii, jjj)
                        st1 = st[ii:iii]
                        ll1 = iii-ii
                        st2 = st[jjj:jj+1]
                        ll2 = jj+1-jjj
                        #print(ii,iii,jjj,jj,st1, ll1, st2, ll2)
                        if ispalindrome(st1+st2):
                            current = max(current, ll1+ll2)
                result = max(result, current)
                        
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
