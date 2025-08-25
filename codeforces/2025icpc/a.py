# -*- coding: utf-8 -*-

"""

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

from collections import defaultdict

def k2(r: int, c: int, r1: int, c1: int, city: list):
    result = 0
    #print(r1, c1, city)
    for cc in range(1, c+1):
        if city[r1][0] == 0:
            continue
        if city[r1][cc] == 0:
            city[r1][cc] = 1
            city[r1][0] -= 1
            city[0][cc] -= 1
            result += k3(r, c, r1, cc, city)
            city[r1][cc] = 0
            city[r1][0] += 1
            city[0][cc] += 1

    for rr in range(1, r+1):
        if city[0][c1] == 0:
            continue
        if city[rr][c1] == 0:
            city[rr][c1] = 1
            city[rr][0] -= 1
            city[0][c1] -= 1
            result += k3(r, c, rr, c1, city)
            city[rr][c1] = 0
            city[rr][0] += 1
            city[0][c1] += 1

    return result

def k3(r: int, c: int, r2: int, c2: int, city: list):
    result = 0
    #print(r2, c2)
    for cc in range(1, c+1):
        if city[r2][cc] == 0:
            city[r2][cc] = 1
            city[r2][0] -= 1
            city[0][cc] -= 1
            result += k4(r, c, r2, cc, city)
            city[r2][cc] = 0
            city[r2][0] += 1
            city[0][cc] += 1

    for rr in range(1, r+1):
        if city[rr][c2] == 0:
            city[rr][c2] = 1
            city[rr][0] -= 1
            city[0][c2] -= 1
            result += k4(r, c, rr, c2, city)
            city[rr][c2] = 0
            city[rr][0] += 1
            city[0][c2] += 1
    return result

def k4(r: int, c: int, r3: int, c3: int, city: list):
    result = 0 + city[0][c3] + city[r3][0]
    return result

def codeforces(r: int, c: int, city: list):
    result = 0
    for rr in range(1, r+1):
        for cc in range(1, c+1):
            if city[rr][cc] == 0:
                city[rr][0] += 1
                city[0][cc] += 1
    #print(city)

    for rr in range(1, r+1):
        if city[rr][0] == 0:
            continue
        for cc in range(1, c+1):
            if city[0][cc] == 0:
                continue
            if city[rr][cc] == 0:
                #print("k1", rr, cc)
                city[rr][cc] = 1
                city[rr][0] -= 1
                city[0][cc] -= 1
                result += k2(r, c, rr, cc, city)
                city[rr][cc] = 0
                city[rr][0] += 1
                city[0][cc] += 1

    return result

if __name__ ==  "__main__":
    r, c = list(map(int, input().split()))
    city = [[0]*(c+1)]
    for _ in range(r):
        line = input()
        rn = [0]*(c+1)
        for ii in range(c):
            if line[ii] == "#":
                rn[ii+1] = -1
        city.append(rn)
    print(codeforces(r, c, city))

