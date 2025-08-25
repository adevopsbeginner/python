# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, s: str):
    result = 0
    countd = 0
    countu = 0
    for each in s:
        if each == "-":
            countd += 1
        elif each == "_":
            countu += 1
    
    countd2 = countd//2
    if countd%2 == 1:
        result = (countd2+1)*countu*countd2
    else:
        result = countd2*countu*countd2
        
    return result
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(codeforces(n, s))
