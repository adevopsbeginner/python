"""
Small Palindrome
Chef has 
X
X ones (
1
1s) and 
Y
Y twos (
2
2s) in his collection. He wants to arrange all of them into the smallest possible palindrome number
†
†
  using all of these ones (
1
1s) and twos (
2
2s).

Help Chef with the answer.

Note: 
X
X and 
Y
Y are both even numbers.

†
†
 A palindromic number is a number that remains the same when its digits are reversed.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case will contain two space-separated integers 
X
X, and 
Y
Y — the amount of ones (
1
1s) and twos (
2
2s) respectively.
Output Format
For each test case, output on a new line the smallest possible palindrome number using 
X
X ones (1s) and 
Y
Y twos (2s).

Constraints
1
≤
T
≤
50
1≤T≤50
0
≤
X
,
Y
≤
10
0≤X,Y≤10
X
X and 
Y
Y are both even
2
≤
X
+
Y
≤
10
2≤X+Y≤10
Sample 1:
Input
Output
2
2 0
2 2
11
1221
Explanation:
Test case 
1
1: The only palindrome number that can be formed using 
2
2 ones (
1
1s) is 
11
11.

Test case 
2
2: Two possible palindromic numbers can be formed using 
2
2 ones (
1
1s) and 
2
2 twos (
2
2s) which are 
1221
1221 and 
2112
2112.
The smaller palindromic number is 
1221
1221, so that is the answer for this case.

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

def solution(x: int, y: int):
    result = ""
    if x == 0:
        result += "2"*y
    else:
        result = "1"*(x//2)+"2"*y+"1"*(x//2)

    print(result)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        line = sys.stdin.readline().strip()
        xy = line.split(" ")
        solution(int(xy[0]), int(xy[1]))
