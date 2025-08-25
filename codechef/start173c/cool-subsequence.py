# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codechef(n: int, arr: []):
    dd = defaultdict(int)
    for each in arr:
        dd[each] += 1
    for each in dd:
        if dd[each] > 1:
            print("1")
            print(each)
            return
    print("-1")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        codechef(n, arr)
        