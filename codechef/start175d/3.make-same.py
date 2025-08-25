# -*- coding: utf-8 -*-

"""
Make same
You are given three binary strings
†
†
  
S
1
,
S
2
,
S
3
S 
1
​
 ,S 
2
​
 ,S 
3
​
  each of length 
N
N. Your goal is to make each string contain identical characters (all 
0
′
s
0 
′
 s or all 
1
′
s
1 
′
 s).

To achieve this, you can perform the following operation:

Choose 
x
,
y
x,y from 
{
1
,
2
,
3
}
{1,2,3}.
Choose index 
i
,
j
i,j such that 
0
≤
i
,
j
<
N
0≤i,j<N.
Swap 
S
x
i
S 
xi
​
  and 
S
y
j
S 
yj
​
  (character at 
i
t
h
i 
th
  index in 
S
x
S 
x
​
  and character at 
j
t
h
j 
th
  index in 
S
y
S 
y
​
 ).
Find the minimum number of operations required to make each string contain identical characters. Print 
−
1
−1 if not possible.

†
†
 A binary string is a sequence of characters where each character is either 
′
0
′
′
 0 
′
  or 
′
1
′
′
 1 
′
 .

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains 
N
N, the length of the string.
The next 
3
3 lines of input contain 
3
3 binary strings.
Output Format
For each test case, output on a new line the minimum number of operations to required to make all strings have same characters, 
−
1
−1 if it is not possible.

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
N
≤
10
1≤N≤10
Sum of 
N
N over all test cases 
≤
1
0
5
≤10 
5
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codechef(n: int, s1: str, s2: str, s3: str):
    count1 = 0
    count2 = 0
    count3 = 0
    for ii in range(n):
        if s1[ii] == "1":
            count1 += 1
        if s2[ii] == "1":
            count2 += 1
        if s3[ii] == "1":
            count3 += 1
    count123 = count1+count2+count3
    if count123 == 0:
        return 0
    if count123 == n:
        return count123-max(count1, count2, count3)
    if count123 == n*2:
        return min(count1, count2, count3)
    if count123 == n*3:
        return 0
    return -1


    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s1 = input()
        s2 = input()
        s3 = input()
        print(codechef(n, s1,s2,s3))
