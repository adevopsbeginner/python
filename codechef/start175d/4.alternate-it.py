# -*- coding: utf-8 -*-

"""
Alternate It!
Given a binary string 
S
S.
You can perform a series of operations on it any number of times:

Odd-numbered operations 
(
1
s
t
,
3
r
d
,
5
t
h
,
.
.
.
)
:
(1 
st
 ,3 
rd
 ,5 
th
 ,...): You can shuffle any (possibly empty) substring
†
†
  of 
S
S in any order.
Even-numbered operations 
(
2
n
d
,
4
t
h
,
6
t
h
,
.
.
.
)
(2 
nd
 ,4 
th
 ,6 
th
 ,...) : You can choose any (possibly empty) substring of 
S
S and flip every bit of it.
Flipping a character means turning it from 
0
0 to 
1
1 and vice versa.
Find the minimum number of operations to be performed to make the string alternating
‡
‡
 .

†
†
 A substring of a string is a contiguous sequence of characters within the string.

‡
‡
 A string is called alternating if no two adjacent characters are the same.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of one line - the binary string 
S
S.
Output Format
For each test case, print a single integer on a new line — the minimum number of operations required to make 
S
S alternating.

Constraints
1
≤
T
≤
1
0
5
1≤T≤10 
5
 
1
≤
∣
S
∣
≤
1
0
5
1≤∣S∣≤10 
5
 
The sum of length of strings over all test cases won't exceed 
1
0
5
10 
5
 .
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


# cook your dish here

def codechef(ss: str):
    ll = len(ss)
    count0 = 0
    count1 = 0
    for each in ss:
        if each == "0":
            count0 += 1
        else:
            count1 += 1
            
    if abs(count0 - count1) <= 1:
        for ii in range(1,ll):
            if ss[ii] == ss[ii-1]:
                return 1
        return 0
    if abs(count0 - count1) == 2:
        return 2
    
    if abs(count0 - count1) == 3:
        return 2

    return 3

    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        ss = input()
        print(codechef(ss))
