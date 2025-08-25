# -*- coding: utf-8 -*-

"""
F. Friends and Pizza
time limit per test8 seconds
memory limit per test512 megabytes
Monocarp has n
 pizzas, the i
-th pizza consists of ai
 slices. Pizzas are denoted by uppercase Latin letters from A to the n
-th letter of the Latin alphabet.

Monocarp also has m
 friends, and he wants to invite exactly two of them to eat pizza. For each friend, Monocarp knows which pizzas that friend likes.

After the friends arrive at Monocarp's house, or each pizza, the following happens:

if the pizza is not liked by any of the two invited friends, Monocarp eats it;
if the pizza is liked by exactly one of the two invited friends, that friend eats it;
and if the pizza is liked by both friends, they try to split it. If it consists of an even number of slices, they both eat exactly half of the slices. But if the pizza consists of an odd number of slices, they start quarrelling, trying to decide who will eat an extra slice — and Monocarp doesn't like that.
For each k
 from 0
 to ∑ai
, calculate the number of ways to choose exactly two friends to invite so that the friends don't quarrel, and Monocarp eats exactly k
 slices.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(self, arr: list):
    ll = len(nums)
    result = 0

    for ii in range(ll):
        pass

    return result

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
