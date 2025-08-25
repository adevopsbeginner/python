# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codechef(x: int, y: int):
    result = x+y*10
    return result
    
if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
        x,y = list(map(int, input().split()))
        print(codechef(x,y))
