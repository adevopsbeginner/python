"""
Streak Star
The Streak Value of an array 
B
B is defined as the maximum length of a non-decreasing subarray, more formally:

max
⁡
1
≤
i
≤
j
≤
N
(
j
−
i
+
1
)
where
B
i
≤
B
i
+
1
≤
B
i
+
2
≤
⋯
≤
B
j
.
1≤i≤j≤N
max
​
 (j−i+1)whereB 
i
​
 ≤B 
i+1
​
 ≤B 
i+2
​
 ≤⋯≤B 
j
​
 .
Chef has an array 
A
A of length 
N
N and a magical number 
X
X. You are allowed to perform the following operation at most once:

Select an index 
i
i, and update the element at 
A
i
A 
i
​
  by multiplying it with 
X
X, i.e., set 
A
i
:
=
A
i
⋅
X
A 
i
​
 :=A 
i
​
 ⋅X
Your task is to find the maximum possible Streak Value achievable for array 
A
A.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two space-separated integers 
N
N and 
X
X — the length of array and magical number respectively.
The second line of each test case contains 
N
N space-separated integers 
A
1
,
A
2
,
A
3
.
.
.
A
N
A 
1
​
 ,A 
2
​
 ,A 
3
​
 ...A 
N
​
  — the elements of the array.
Output Format
For each test case, output on a new line the maximum possible Streak Value of 
A
A.

Constraints
1
≤
T
≤
1
0
3
1≤T≤10 
3
 
1
≤
N
,
X
≤
1
0
3
1≤N,X≤10 
3
 
1
≤
A
i
≤
1
0
5
1≤A 
i
​
 ≤10 
5
 
The sum of 
N
N over all test cases won't exceed 
1
0
3
10 
3
 .
Sample 1:
Input
Output
3
5 3
1 2 1 4 2
3 10
2 5 3
4 5
90 2 5 6
4
3
3
Explanation:
Test case 
1
1: It is optimal to select index 
3
3, which changes the array 
A
A to 
[
1
,
2
,
3
,
4
,
2
]
[1,2,3,4,2]. The Streak Value for the array 
[
1
,
2
,
3
,
4
,
2
]
[1,2,3,4,2] is 
4
4, as the longest non-decreasing subarray is 
[
1
,
2
,
3
,
4
]
[1,2,3,4].

Test case 
2
2: Its optimal to select index 
3
3, which changes the array 
A
A to 
[
2
,
5
,
30
]
[2,5,30].
The Streak Value for the array 
[
2
,
5
,
30
]
[2,5,30] is 
3
3, as the entire array is already non-decreasing.

Test case 
3
3: In this case, it is optimal to either not perform any operation or perform the operation on index 
4
4, both of which result in a Streak Value of 
3
3.

Did you like the problem statement?
More Info
Time limit1 secs
Memory limit1.5 GB
Source Limit50000 Bytes
"""

import string
import heapq
from typing import List
from collections import defaultdict

# cook your dish here
import sys

def solution(n: int, x: int, q: []):
    result = 0
    q = [min(q)-1] + q + [min(q)-1]
    for ii in range(1,n+1):
        q[ii] *= x
        #print(n,x,q)
        count = 0
        for jj in range(1, n+2):
            #print(n,x,ii,jj,q,count,result)
            if q[jj] >= q[jj-1]:
                count += 1
            else:
                result = max(result,count)
                count = 1
            
        q[ii] //= x

    print(result)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()
        n,x = line1.split(" ")
        q = line2.split(" ")
        for ii in range(int(n)):
            q[ii] = int(q[ii])
        solution(int(n), int(x), q)
