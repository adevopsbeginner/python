# -*- coding: utf-8 -*-

"""
Graph Monsters
You are given a connected, undirected graph consisting of 
N
N nodes and 
M
M edges. Every node has a pass value of 
A
i
A 
i
​
  and a monster with health 
B
i
B 
i
​
 .

Your task is to defeat all the monsters eventually. To do that, you can do the following steps:

Choose a starting node 
S
S (
1
≤
S
≤
N
1≤S≤N) and a starting health value 
H
H.
Suppose your current node is 
X
X, you can either battle the monster (if it has not been fought already) or go to a different node. Both the actions have some restrictions. Specifically,
If you choose to battle the monster, 
H
≥
B
i
H≥B 
i
​
  must hold. After fighting this monster, your health changes to 
H
−
B
i
H−B 
i
​
 .
If you choose to go to a different node 
Y
Y, there must be an edge between 
X
X and 
Y
Y. Further, your health must be greater than the pass values of both nodes 
X
X and 
Y
Y, i.e. 
H
≥
A
X
H≥A 
X
​
  and 
H
≥
A
Y
H≥A 
Y
​
 .
Find the minimum possible starting health value 
H
H such that it is possible to beat all monsters. You may choose to start at any node.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two space-separated integers 
N
N and 
M
M — the number of vertices and edges of the graph, respectively.
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
 , the pass values of each node.
The third line contains 
N
N integers - 
B
1
,
B
2
,
.
.
.
,
B
N
B 
1
​
 ,B 
2
​
 ,...,B 
N
​
 , the monster healths of each node.
The next 
M
M lines describe the edges. The 
i
i-th of these 
M
M lines contains two space-separated integers 
u
i
u 
i
​
  and 
v
i
v 
i
​
 , denoting an edge between 
u
i
u 
i
​
  and 
v
i
v 
i
​
 .
Output Format
For each test case, output on a new line the minimum starting health value.

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
 
2
≤
N
≤
2
⋅
1
0
5
2≤N≤2⋅10 
5
 
N
−
1
≤
M
≤
min
⁡
(
N
⋅
(
N
−
1
)
2
,
2
⋅
1
0
5
)
N−1≤M≤min( 
2
N⋅(N−1)
​
 ,2⋅10 
5
 )
1
≤
A
i
,
B
i
≤
1
0
9
1≤A 
i
​
 ,B 
i
​
 ≤10 
9
 
1
≤
u
i
,
v
i
≤
N
1≤u 
i
​
 ,v 
i
​
 ≤N
u
i
≠
v
i
u 
i
​
 =v 
i
​
 
All the 
M
M unordered pairs 
(
u
i
,
v
i
)
(u 
i
​
 ,v 
i
​
 ) are different.
The sum of 
N
N and the sum of 
M
M both do not exceed 
2
⋅
1
0
5
2⋅10 
5
  over all test cases.
Sample 1:
Input
Output
5
3 2
1 1 1
3 2 4
1 2
2 3
2 1
60 72
48 56
1 2
4 6
10 12 4 3
3 7 5 8
1 2
1 3
1 4
2 3
2 4
3 4
4 6
10 12 5 8
3 7 4 3
1 2
1 3
1 4
2 3
2 4
3 4
6 6
60 55 50 45 40 75
17 28 39 32 14 54
1 2
5 6
3 4
3 5
1 6
2 3
9
120
23
21
195
Explanation:
Test Case 1 : Start with health 
H
=
9
H=9 at vertex 
1
1 and perform the following moves:

Kill the monster at node 
3
3. 
H
=
9
−
4
=
5
H=9−4=5.
Move to node 
2
2 (
H
≥
A
2
H≥A 
2
​
  and 
H
≥
A
3
H≥A 
3
​
  are satisfied).
Kill the monster at 
2
2. 
H
=
5
−
2
H=5−2.
Move to node 
1
1 (
H
≥
A
1
H≥A 
1
​
  and 
H
≥
A
2
H≥A 
2
​
  are satisfied).
Kill the monster at 
1
1. 
H
=
2
−
2
=
0
H=2−2=0.
You have successfully defeated all monsters.

Test case 2 : Start at vertex 
1
1 with 
120
120 health, kill the monster here, move to vertex 
2
2 and kill the monster there.

With a smaller initial health value, it is not possible to move between the 
2
2 nodes after killing a monster regardless of starting at 
1
1 or 
2
2. Hence, the answer is 
120
120.
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
