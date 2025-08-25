# -*- coding: utf-8 -*-

"""
B. Two Large Bags
time limit per test1 second
memory limit per test256 megabytes

You have two large bags of numbers. Initially, the first bag contains n
 numbers: a1,a2,…,an
, while the second bag is empty. You are allowed to perform the following operations:

Choose any number from the first bag and move it to the second bag.
Choose a number from the first bag that is also present in the second bag and increase it by one.
You can perform an unlimited number of operations of both types, in any order. Is it possible to make the contents of the first and second bags identical?

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains an integer n
 (2≤n≤1000
) — the length of the array a
. It is guaranteed that n
 is an even number.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤n
).

It is guaranteed that the sum of n2
 over all test cases does not exceed 106
.

Output
For each test case, print "YES" if it is possible to equalize the contents of the bags. Otherwise, output "NO".

You can output each letter in any case (for example, "YES", "Yes", "yes", "yEs", "yEs" will be recognized as a positive answer).

Example
InputCopy
9
2
1 1
2
2 1
4
1 1 4 4
4
3 4 3 3
4
2 3 4 4
6
3 3 4 5 3 3
6
2 2 2 4 4 4
8
1 1 1 1 1 1 1 4
10
9 9 9 10 10 10 10 10 10 10
OutputCopy
Yes
No
Yes
Yes
No
Yes
No
Yes
Yes
Note
Let's analyze the sixth test case: we will show the sequence of operations that leads to the equality of the bags. Initially, the first bag consists of the numbers (3,3,4,5,3,3)
, and the second bag is empty.

In the first operation, move the number 3
 from the first bag to the second. State: (3,4,5,3,3)
 and (3)
.
In the second operation, increase the number 3
 from the first bag by one. This operation is possible because the second bag contains the number 3
. State: (4,4,5,3,3)
 and (3)
.
In the third operation, move the number 4
 from the first bag to the second. State: (4,5,3,3)
 and (3,4)
.
In the fourth operation, increase the number 4
 from the first bag by one. State: (5,5,3,3)
 and (3,4)
.
In the fifth operation, move the number 5
 from the first bag to the second. State: (5,3,3)
 and (3,4,5)
.
In the sixth operation, increase the number 3
 from the first bag by one. State: (5,3,4)
 and (3,4,5)
.
As we can see, as a result of these operations, it is possible to make the contents of the bags equal, so the answer exists.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: []):
    result = "no"
    dd = defaultdict(int)
    for each in arr:
        dd[each] += 1
    larr = list(dd.keys())
    larr.sort()

    while len(larr) > 0:
        ll = len(larr)
        if dd[larr[0]] == 1:
            return "no"
        if ll == 1:
            if dd[larr[0]]%2 == 0:
                return "yes"
            else:
                return "no"
        if larr[0] + 1 == larr[1]:
            dd[larr[1]] += dd[larr[0]]-2
            larr.pop(0)
        else:
            dd[larr[0]+1] = dd[larr[0]]-2
            dd[larr[0]] = 2
            larr[0] += 1

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(codeforces(n,a))
    # print(codeforces(2, [1, 1]))
    # print(codeforces(2, [2, 1]))
    # print(codeforces(4, [1, 1, 4, 4]))
    # print(codeforces(4, [3, 4, 3, 3]))
    # print(codeforces(4, [2, 3, 4, 4]))
    # print(codeforces(6, [3, 3, 4, 5, 3, 3]))
    # print(codeforces(6, [2, 2, 2, 4, 4, 4]))
    # print(codeforces(8, [1, 1, 1, 1, 1, 1, 1, 4]))
    # print(codeforces(10, [9, 9, 9, 10, 10, 10, 10, 10, 10, 10]))
