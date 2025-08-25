# -*- coding: utf-8 -*-

"""
D. Palindrome Shuffle
time limit per test2 seconds
memory limit per test256 megabytes
You are given a string s
 consisting of lowercase Latin letters.

You can perform the following operation with the string s
: choose a contiguous substring (possibly empty) of s
 and shuffle it (reorder the characters in the substring as you wish).

Recall that a palindrome is a string that reads the same way from the first character to the last and from the last character to the first. For example, the strings a, bab, acca, bcabcbacb are palindromes, but the strings ab, abbbaa, cccb are not.

Your task is to determine the minimum possible length of the substring on which the aforementioned operation must be performed in order to convert the given string s
 into a palindrome.

Input
The first line contains a single integer t
 (1≤t≤104
) — the number of test cases.

The only line of each test case contains a string s
 (2≤|s|≤2⋅105
), consisting of lowercase Latin letters.

Additional constraints on the input:

the string s
 has an even length;
the string s
 can always be converted to a palindrome;
the sum of lengths of s
 over all test cases doesn't exceed 2⋅105
.
Output
For each test case, print a single integer — the minimum possible length of the substring on which the aforementioned operation must be performed in order to convert the given string s
 into a palindrome.

Example
InputCopy
4
baba
cc
ddaa
acbacddacbca
OutputCopy
2
0
3
2
Note
In the first example, you can perform the operation as follows: baba →
 baab.

In the second example, the string is already a palindrome, so we can shuffle an empty substring.

In the third example, you can perform the operation as follows: ddaa →
 adda.

In the fourth example, you can perform the operation as follows: acbacddacbca →
 acbcaddacbca.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(s: str):
    ll = len(s)
    ll2 = ll//2
    first = -1
    last = 0
    for ii in range(ll2):
        if s[ii] != s[ll-1-ii]:
            if first < 0:
                first = ii
            last = ii
 
    if first < 0:
        return 0
        
    dd1 = defaultdict(int)
    dd2 = defaultdict(int)
    for ii in range(ll2):
        dd1[s[ii]] += 1
    for ii in range(ll2,ll):
        dd2[s[ii]] += 1
    for each in dd1:
        if dd1[each] != dd2[each]:
            if first == 0:
                return ll-1
            else:
                return 2*(last-first+1)
 
    return last-first+1
    
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(codeforces(s))