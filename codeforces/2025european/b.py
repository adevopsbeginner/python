# -*- coding: utf-8 -*-

"""
B. Urban Planning
time limit per test2 seconds
memory limit per test1024 megabytes
You are responsible for planning a new city! The city will be represented by a rectangular grid, where each cell is either a park or a built-up area.

The residents will naturally want to go for walks in the city parks. In particular, a rectangular walk is a rectangle consisting of the grid cells, which is at least 2 cells long both horizontally and vertically, such that all cells on the boundary of the rectangle are parks. Note that the cells inside the rectangle can be arbitrary.

An example rectangular walk (cells with dark background).
Your favourite number is k
. To leave a long-lasting signature, you want to design the city in such a way that it has exactly k
 rectangular walks.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: list):

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
