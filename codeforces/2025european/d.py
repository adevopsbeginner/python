# -*- coding: utf-8 -*-

"""
D. Morse Code
time limit per test2 seconds
memory limit per test1024 megabytes
Morse code is a classical way to communicate over long distances, but there are some drawbacks that increase the transmission time of long messages.

In Morse code, each character in the alphabet is assigned a sequence of dots and dashes such that no sequence is a prefix of another. To transmit a string of characters, the sequences corresponding to each character are sent in order. A dash takes twice as long to transmit as a dot.

Your alphabet has n
 characters, where the i
-th character appears with frequency fi
 in your language. Your task is to design a Morse code encoding scheme, assigning a sequence of dots and dashes to each character, that minimizes the expected transmission time for a single character. In other words, you want to minimize f1t1+f2t2+⋯+fntn
, where ti
 is the time required to transmit the sequence of dots and dashes assigned to the i
-th character.
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
