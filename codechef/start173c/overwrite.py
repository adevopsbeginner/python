# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def compare(a: [], b: []):
    lla = len(a)
    llb = len(b)
    for ii in range(min(lla,llb)):
        if a[ii] == b[ii]:
            continue
        elif a[ii] < b[ii]:
            return -1
        elif a[ii] > b[ii]:
            return 1
    return 0
    
def codechef(n: int, m: int, a: [], b:[]):
    lla = len(a)
    llb = len(b)
    minb = min(b)
    for ii in range(llb):
        if b[ii] == minb:
            if compare(b[ii:]+b[:ii], b) == -1:
                b = b[ii:]+b[:ii]
    for ii in range(lla-llb+1):
        if compare(a[ii:ii+llb], b) == 1:
            for jj in range(llb):
                a[ii+jj] = b[jj]
    return a
