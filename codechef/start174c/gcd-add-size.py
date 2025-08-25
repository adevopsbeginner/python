# -*- coding: utf-8 -*-

"""
GCD Add Size
You’re given a sequence 
A
A of size 
N
N. Your task is to choose a non-empty subsequence 
B
B of 
A
A to maximize 
f
(
B
)
f(B).

Here, 
f
(
B
)
f(B) is defined as 
∣
B
∣
+
g
c
d
(
B
1
,
B
2
,
…
,
B
∣
B
∣
)
∣B∣+gcd(B 
1
​
 ,B 
2
​
 ,…,B 
∣B∣
​
 ), where 
∣
B
∣
∣B∣ is the size of 
B
B and 
g
c
d
(
B
1
,
B
2
,
…
,
B
∣
B
∣
)
gcd(B 
1
​
 ,B 
2
​
 ,…,B 
∣B∣
​
 ) is the greatest common divisor of all numbers in 
B
B.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains an integer 
N
N.
The second line contains 
N
N space-separated integers 
A
1
,
A
2
,
⋯
 
,
A
N
A 
1
​
 ,A 
2
​
 ,⋯,A 
N
​
 .
Output Format
For each test case, output on a new line - the maximum value of 
f
(
B
)
f(B).

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
4
⋅
1
0
5
1≤N≤4⋅10 
5
 
1
≤
A
i
≤
1
0
12
1≤A 
i
​
 ≤10 
12
 
The sum of 
N
N over all test cases won't exceed 
4
⋅
1
0
5
4⋅10 
5
 .
Sample 1:
Input
Output
2
4
1 2 3 6
6
6 1 3 3 3 3
7
8
Explanation:
Test case 
1
1: It is optimal to choose 
B
=
[
6
]
B=[6].

Test case 
2
2: It is optimal to choose 
B
=
[
6
,
3
,
3
,
3
,
3
]
B=[6,3,3,3,3].
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codechef(n: int, arr: list):
    ll = len(arr)
    result = 0

    for ii in range(ll):
        pass

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(codechef(n, a))

    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     stra = sys.stdin.readline().strip()
    #     strb = sys.stdin.readline().strip()
    #     codechef(stra,strb)
