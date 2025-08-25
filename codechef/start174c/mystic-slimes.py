# -*- coding: utf-8 -*-

"""
Mystic Slimes
There are 
N
N mystic slimes arranged in a line, and the power of the 
i
i-th slime is 
A
i
A 
i
​
 .

You need to perform the following operations until only one slime remains:

Choose two adjacent indices 
i
i, 
j
j (
1
≤
i
,
j
≤
∣
A
∣
1≤i,j≤∣A∣, 
∣
i
−
j
∣
=
1
∣i−j∣=1), and let the 
i
i-th slime eat the 
j
j-th slime. After this operation, the power of the 
i
i-th slime becomes 
max
⁡
(
0
,
A
i
−
A
j
)
max(0,A 
i
​
 −A 
j
​
 ) (while the 
j
j-th slime is removed).
Here, it is not necessary that 
A
i
≥
A
j
A 
i
​
 ≥A 
j
​
 , i.e. even a smaller slime can eat a bigger slime.
Note that after each operation, the number of slimes decreases by 
1
1, and all slimes are reindexed starting from 
1
1. The relative order between uneaten slimes remains unchanged.

Find the maximum possible power of the last remaining slime.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test contains 
N
N - the size of the array.
The second line contains 
N
N integers - 
A
1
,
A
2
,
.
.
.
,
A
N
A 
1
​
 ,A 
2
​
 ,...,A 
N
​
 .
Output Format
For each test case, output on a new line the maximum possible power of the last remaining slime.

Constraints
1
≤
T
≤
1000
1≤T≤1000
2
≤
N
≤
50
2≤N≤50
1
≤
A
i
≤
1000
1≤A 
i
​
 ≤1000
Sample 1:
Input
Output
5
2
1 2
3
1 2 3
3
1 100 10
2
1000 1000
4
1 1 1 1
1
3
89
0
1
Explanation:
Test Case 1 : We choose indices 
i
=
2
,
j
=
1
i=2,j=1 and let 
2
2nd slime eat the 
1
1st. Now, the new power of the 
2
2nd slime becomes 
1
1 (and it is re-indexed to position 
1
1). Since only one slime remains, the answer here is 
1
1.

Test Case 2 : We perform the following steps:

A
=
[
1
,
2
,
3
]
A=[1,2,3], pick 
i
=
1
,
j
=
2
i=1,j=2. The updated powers are 
[
0
,
3
]
[0,3].
A
=
[
0
,
3
]
A=[0,3], pick 
i
=
2
,
j
=
0
i=2,j=0. The updated power of the last remaining slime is 
3
3.
Hence, the answer is 
3
3.
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
