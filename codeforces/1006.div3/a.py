# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n,k,p):
    k = abs(k)
    if n*p < k:
        return -1
 
    result = k//p
    if k%p > 0:
        result += 1
        
    return result
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,k,p = list(map(int, input().split()))
        print(codeforces(n, k, p))
