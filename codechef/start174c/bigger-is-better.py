# -*- coding: utf-8 -*-

"""
Bigger is Better
Chef is setting up a new restaurant in Chefland, and has to decide on a name for it.
In Chefland, all restaurants must have names that are of length exactly 
N
N, consisting of lowercase English letters.

Unfortunately for Chef, there's a competing restaurant right across the street!
This competitor has a name represented by the string 
A
A, which consists of only lowercase English letters.

Chef believes that bigger is better — so he wants his restaurant's name to be lexicographically larger
†
†
  than 
A
A.
In fact, to go even further beyond, he wants to be larger no matter which direction the name is read in: so he also wants the reverse of his restaurant's name to be lexicographically larger than 
A
A.

Help Chef find any valid name for his restaurant, or tell him that no valid names exist.

†
†
  String 
P
P of length 
N
N is lexicographically larger than another string 
Q
Q of the same length if and only if there exists an index 
i
i (
1
≤
i
≤
N
1≤i≤N) such that:

P
i
>
Q
i
P 
i
​
 >Q 
i
​
 ; and
P
j
=
Q
j
P 
j
​
 =Q 
j
​
  for all 
1
≤
j
<
i
1≤j<i
Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains a single integer 
N
N, the length of restaurant names in Chefland.
The second line contains a string 
A
A of length 
N
N, the name of the competing restaurant.
Output Format
For each test case,

If no solution exists, print the single integer 
−
1
−1 on a new line.
Otherwise, output a single string of length 
N
N, consisting of lowercase English letters: a valid name for Chef's restaurant.
If there are multiple possible answers, any of them will be accepted.

Constraints
1
≤
T
≤
100
1≤T≤100
1
≤
N
≤
100
1≤N≤100
A
i
∈
{
a, b, 
…
,
z
}
A 
i
​
 ∈{a, b, …,z}
Sample 1:
Input
Output
4
8
codechef
4
five
1
z
7
rallets
topcoder
four
-1
specter
Explanation:
Test case 
1
1: "topcoder" is lexicographically larger than "codechef". The reverse of "topcoder" is "redocpot" which is also lexicographically larger than "codechef".
So, this is a valid name for the restaurant.

Test case 
3
3: It can be proved that no valid name exists.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


# cook your dish here

def codechef(n: int, s: str):
    new_name = "z"*n
    if new_name == s:
        return "-1"
    return new_name


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(codechef(n, s))

    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     stra = sys.stdin.readline().strip()
    #     strb = sys.stdin.readline().strip()
    #     codechef(stra,strb)
