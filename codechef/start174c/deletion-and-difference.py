# -*- coding: utf-8 -*-

"""
Deletion and Difference
You're given an array 
A
A of length 
N
N. You can perform the following operation on it:

Choose two indices 
i
i and 
j
j (
1
≤
i
<
j
≤
∣
A
∣
1≤i<j≤∣A∣) such that 
A
i
=
A
j
A 
i
​
 =A 
j
​
 .
Delete both 
A
i
A 
i
​
  and 
A
j
A 
j
​
  from 
A
A, and append 
∣
A
i
−
A
j
∣
∣A 
i
​
 −A 
j
​
 ∣ to 
A
A.
The length of the array reduces by 
1
1, and all remaining elements are re-indexed to start from 
1
1.
Find the minimum possible length of 
A
A after performing this operation several (possibly, zero) times.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains a single integer 
N
N, denoting the length of 
A
A.
The second line contains 
N
N space-separated integers 
A
1
,
A
2
,
…
,
A
N
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
  — the elements of 
A
A.
Output Format
For each test case, output on a new line a single integer: the minimum possible length of 
A
A after performing the given operation several times.

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
2
⋅
1
0
5
1≤N≤2⋅10 
5
 
0
≤
A
i
≤
N
0≤A 
i
​
 ≤N
The sum of 
N
N over all test cases won't exceed 
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
3
4
3 1 4 2
2
1 1
3
1 1 0
4
1
1
Explanation:
Test Case 1 : There are no deletions we can do. Hence, the answer is 
4
4, the size of the initial array.

Test Case 2 : We can choose 
i
=
1
,
j
=
2
i=1,j=2. Note that 
A
1
=
A
2
=
1
A 
1
​
 =A 
2
​
 =1, and then insert their difference 
0
0 back into the array while deleting the 
1
1s. Thus, the final array becomes 
[
0
]
[0] of size 
1
1.
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
