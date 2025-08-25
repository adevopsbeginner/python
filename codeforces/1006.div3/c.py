# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, x: int):
    if n == 1:
        return x
    if n == 2:
        return "0 " + str(x)
        
    result = [0]*n
    for ii in range(31):
        if x & (1<<ii) == 0:
            if n >= 2**ii:
                for jj in range(2**ii):
                    result[jj] =jj
                result[-1] = x
            else:
                for jj in range(n):
                    result[jj] = jj
                for kk in range(ii):
                    if 2**kk > n:
                        if x > 2**kk-1:
                            result[-1] = x
                            break
            break
            
    
    sss = str(result[0])
    for ii in range(1,n):
        sss += " "+str(result[ii])
    return sss
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = list(map(int, input().split()))
        print(codeforces(n, x))
        #codeforces(n, x)
