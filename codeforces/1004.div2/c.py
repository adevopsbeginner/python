# -*- coding: utf-8 -*-

"""
C. Devyatkino
time limit per test2 seconds
memory limit per test256 megabytes
You are given a positive integer n
. In one operation, you can add to n
 any positive integer whose decimal representation contains only the digit 9
, possibly repeated several times.

What is the minimum number of operations needed to make the number n
 contain at least one digit 7
 in its decimal representation?

For example, if n=80
, it is sufficient to perform one operation: you can add 99
 to n
, after the operation n=179
, which contains the digit 7
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The only line of each test case contains an integer n
 (10≤n≤109
).

Output
For each test case, output the minimum number of operations required for the number n
 to contain the digit 7
.

Example
InputCopy
16
51
60
61
777
12345689
1000000000
2002
3001
977
989898986
80
800001
96
70
15
90
OutputCopy
3
2
1
0
1
3
5
4
0
7
1
2
7
0
7
3
Note
In the first test case, three operations are sufficient: 51+9+9+9=78
, which contains the digit 7
. It can be shown that it is impossible to achieve the goal in one or two operations.

In the second test case, two operations are sufficient: 60+9+9=78
.

In the third test case, one operation is sufficient: 61+9=70
.

In the fourth test case, n
 already contains the digit 7
, so no operations are required.

In the fifth test case, you can add 99
 to n
 to obtain a number containing the digit 7
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

from collections import deque

def min_operations_to_7(n):
    queue = deque([(n, 0)])  # (current number, steps taken)
    visited = set()
    
    while queue:
        num, steps = queue.popleft()
        
        # Check if the number contains the digit '7'
        if '7' in str(num):
            return steps
        
        # Try adding numbers consisting of only '9's
        for nine in [9, 99, 999, 9999, 99999]:  # Limited to reasonable values
            new_num = num + nine
            if new_num not in visited:
                visited.add(new_num)
                queue.append((new_num, steps + 1))
    
    return -1  # This case should never happen

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = t = int(input())
        print(codeforces(n))
