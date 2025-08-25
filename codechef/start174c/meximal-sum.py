# -*- coding: utf-8 -*-

"""
Meximal Sum
You are given an integer array 
A
A containing 
N
N elements.

A pair 
(
L
,
R
)
(L,R),
(
1
≤
L
<
R
<
N
)
(1≤L<R<N) is called good pair if:

MEX 
(
A
[
1
,
⋯
L
]
)
(A[1,⋯L]) 
=
= MEX
(
A
[
L
+
1
⋯
R
]
)
(A[L+1⋯R]) 
=
= MEX
(
A
[
R
+
1
⋯
N
]
)
(A[R+1⋯N])
where MEX of an array denotes the minimal non-negative integer which is not present in that array.

Now Your task is to find both minimum and maximum value of SUM
(
A
[
1
⋯
L
]
)
(A[1⋯L]) 
−
− SUM
(
A
[
L
+
1
⋯
R
]
)
(A[L+1⋯R]) 
+
+ SUM
(
A
[
R
+
1
⋯
N
]
)
(A[R+1⋯N]) for any good pair 
L
L and 
R
R.

SUM
A
(
[
X
,
Y
]
)
A([X,Y]) denotes 
A
X
+
A
X
+
1
+
.
.
.
+
A
Y
A 
X
​
 +A 
X+1
​
 +...+A 
Y
​
 .

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains 
N
N - the size of the array.
The second line of each test case contains 
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
For each test case, print the minimum and maximum value of the expression : SUM
(
A
[
1
⋯
L
]
)
(A[1⋯L]) 
−
− SUM
(
A
[
L
+
1
⋯
R
]
)
(A[L+1⋯R]) 
+
+ SUM
(
A
[
R
+
1
⋯
N
]
)
(A[R+1⋯N]) for any good pair 
L
L and 
R
R.

If no good pair exists, print 
−
1
−
1
−1−1.

Constraints
1
≤
T
≤
1
0
4
1≤T≤10 
4
 
3
≤
N
≤
2
⋅
1
0
5
3≤N≤2⋅10 
5
 
0
≤
A
i
≤
1
0
9
0≤A 
i
​
 ≤10 
9
 
The sum of 
N
N over all test cases does not exceed 
2
⋅
1
0
5
2⋅10 
5
 .
Sample 1:
Input
Output
5
3
2 4 3
5
0 9 2 0 1
5
2 3 1 5 3
6
0 1 0 1 0 1
8
0 1 0 1 0 1 0 1
1 1
-1 -1
-4 12
1 1
0 2
Explanation:
Test case 1 : There is only one good pair 
L
=
1
,
R
=
2
L=1,R=2, and MEX of the 
3
3 parts of the array are all 
0
0. For this pair, the value is 
2
−
4
+
3
=
1
2−4+3=1. This is both the minimum and maximum.

Test Case 2 : It can be proven that there is no good pair in this case.
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
