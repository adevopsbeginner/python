# -*- coding: utf-8 -*-

"""
G - Dense Buildings / 
Time Limit: 5 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
600 points

Problem Statement
There is a city divided into 
H×W blocks in the north-south-east-west directions, and there is exactly one building in each block.
Specifically, in the block at the 
i-th row from the north 
(1≤i≤H) and the 
j-th column from the west 
(1≤j≤W) (hereafter referred to as block 
(i,j)), there is a building of 
F 
i,j
​
  floors.

Takahashi has two ways of moving. If he is on the 
X-th floor 
(1≤X≤F 
i,j
​
 ) of the building in block 
(i,j), he can:

Move up or down one floor within the same building using stairs. If 
X=1, he cannot move down; if 
X=F 
i,j
​
 , he cannot move up.
Choose a building with at least 
X floors in a cardinally adjacent block, and move to the 
X-th floor of that building using a (sky) walkway.
Here, two blocks 
(i,j) and 
(i 
′
 ,j 
′
 ) are cardinally adjacent if and only if 
∣i−i 
′
 ∣+∣j−j 
′
 ∣=1.

You are given 
Q queries to be answered. The 
i-th query 
(1≤i≤Q) is the following.

Find the minimum possible number of times that Takahashi uses stairs to move from the 
Y 
i
​
 -th floor of the building in block 
(A 
i
​
 ,B 
i
​
 ) to the 
Z 
i
​
 -th floor of the building in block 
(C 
i
​
 ,D 
i
​
 ).
The count of times using stairs is incremented each time he moves up or down one floor, possibly multiple times within the same building. (For example, moving from the 1st floor to the 6th floor of a building counts as 
5 uses of stairs.)
Note that he does not have to minimize the number of times he uses walkways.

Constraints
1≤H≤500
1≤W≤500
1≤F 
i,j
​
 ≤10 
6
 
1≤Q≤2×10 
5
 
1≤A 
i
​
 ,C 
i
​
 ≤H
1≤B 
i
​
 ,D 
i
​
 ≤W
1≤Y 
i
​
 ≤F 
A 
i
​
 ,B 
i
​
 
​
 
1≤Z 
i
​
 ≤F 
C 
i
​
 ,D 
i
​
 
​
 
(A 
i
​
 ,B 
i
​
 ,Y 
i
​
 )

=(C 
i
​
 ,D 
i
​
 ,Z 
i
​
 )
All input values are integers.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(n: int, arr: list):
    ll = len(arr)
    result = 0

    for ii in range(ll):
        pass

    return result


if __name__ == "__main__":
  t = int(input())
  for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(atcoder(n,arr))
