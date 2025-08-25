# -*- coding: utf-8 -*-

"""
Multiplexer
You are given an array 
A
A of length 
N
N and a positive integer 
X
X. You are allowed to perform the following operation at most once:

Choose any contiguous subarray of 
A
A and multiply each element of the subarray by 
X
X.
Your task is to determine the maximum possible frequency of any element in the array after performing the operation at most once. The frequency of an element is defined as the number of times it appears in the array.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains two space-separated integers 
N
N and 
X
X — the length of array and the multiplier, respectively.
The next line contains 
N
N space-separated integers 
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
  — the elements of the array.
Output Format
For each test case, output a single line containing one integer — the maximum frequency of any element that can be achieved after performing the operation at most once.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


# cook your dish here

#from collections import defautdict

def codechef(n: int, x: int, arr: list):
    result = 0
    dd = {}
    for each in arr:
        if each not in dd:
            dd[each] = 1
        else:
            dd[each] += 1
        
    result = 0
    for each in dd:
        result = max(result, dd[each])
        
    if x == 1:
        return result
        
    for each in dd:
        if each*x in dd:
            if dd[each*x] + dd[each] > result:
                result = dd[each*x] + dd[each]

    return result

    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        print(codechef(n, x, arr))

    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     stra = sys.stdin.readline().strip()
    #     strb = sys.stdin.readline().strip()
    #     codechef(stra,strb)
