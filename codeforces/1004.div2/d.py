# -*- coding: utf-8 -*-

"""
D. Object Identification
time limit per test2 seconds
memory limit per test256 megabytes

This is an interactive problem.

You are given an array x1,…,xn
 of integers from 1
 to n
. The jury also has a fixed but hidden array y1,…,yn
 of integers from 1
 to n
. The elements of array y
 are unknown to you. Additionally, it is known that for all i
, xi≠yi
, and all pairs (xi,yi)
 are distinct.

The jury has secretly thought of one of two objects, and you need to determine which one it is:

Object A: A directed graph with n
 vertices numbered from 1
 to n
, and with n
 edges of the form xi→yi
.
Object B: n
 points on a coordinate plane. The i
-th point has coordinates (xi,yi)
.
To guess which object the jury has thought of, you can make queries. In one query, you must specify two numbers i,j
 (1≤i,j≤n,i≠j)
. In response, you receive one number:

If the jury has thought of Object A, you receive the length of the shortest path (in edges) from vertex i
 to vertex j
 in the graph, or 0
 if there is no path.
If the jury has thought of Object B, you receive the Manhattan distance between points i
 and j
, that is |xi−xj|+|yi−yj|
.
You have 2
 queries to determine which of the objects the jury has thought of.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤1000
). The description of the test cases follows.

Interaction
The interaction begins with reading n
 (3≤n≤2⋅105
) — the length of the arrays x
 and y
 at the start of each test case.

Next, read n
 integers: x1,x2,…,xn
 (1≤xi≤n
) — the elements of array x
.

It is guaranteed that the sum of n
 across all test cases does not exceed 2⋅105
.

The array y1,y2,…,yn
 is fixed for each test case. In other words, the interactor is not adaptive.

It is guaranteed that xi≠yi
 for all 1≤i≤n
, and all pairs (xi,yi)
 are distinct.

To make a query, output "? i
 j
" (without quotes, 1≤i,j≤n,i≠j
). Then you must read the response to the query, which is a non-negative integer.

To give an answer, output "! A" if Object A is hidden or "! B" if Object B is hidden (without quotes). Note that printing the answer does not count as one of the 2
 queries.

After printing each query do not forget to output the end of line and flush∗
 the output. Otherwise, you will get Idleness limit exceeded verdict. If, at any interaction step, you read −1
 instead of valid data, your solution must exit immediately. This means that your solution will reveive Wrong answer because of an invalid query or any other mistake. Failing to exit can result in an arbitrary verdict because your solution will continue to read from a closed stream. Note that if the query is correct, the response will never be −1
.

Hacks

The first line must contain an integer t
 (1≤t≤1000
) — the number of test cases.

The first line of each test case must contain an integer n
 (3≤n≤2⋅105
) — the length of the hidden array.

The second line of each test case must contain n
 integers — x1,x2,…,xn
 (1≤xi≤n
).

The third line of each test case must contain n
 integers — y1,y2,…,yn
 (1≤yi≤n
).

It must be ensured that xi≠yi
 for all 1≤i≤n
, and all pairs (xi,yi)
 must be distinct.

The fourth line must contain one character: A or B, indicating which of the objects you want to hide.

The sum of n
 across all test cases must not exceed 2⋅105
.

∗
To flush, use:

fflush(stdout) or cout.flush() in C++;
sys.stdout.flush() in Python;
see the documentation for other languages.
Example
InputCopy
2
3
2 2 3

1

0

5
5 1 4 2 3

4

4
OutputCopy
? 2 3

? 1 2

! A

? 1 5

? 5 1

! B
Note
In the first test case, x=[2,2,3]
, y=[1,3,1]
 and Object A is guessed.

In the second test case, x=[5,1,4,2,3]
, y=[3,3,2,4,1]
 and Object B is guessed.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(self, head: Optional[ListNode]) -> List[int]:
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
