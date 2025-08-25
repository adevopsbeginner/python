# -*- coding: utf-8 -*-

"""
E. Game with Binary String
time limit per test3 seconds
memory limit per test512 megabytes
Consider the following game. Two players have a binary string (a string consisting of characters 0 and/or 1). The players take turns, the first player makes the first turn. During a player's turn, he or she has to choose exactly two adjacent elements of the string and remove them (the first element and the last element are also considered adjacent). Furthermore, there are additional constraints depending on who makes the move:

if it's the first player's move, both chosen characters should be 0;
if it's the second player's move, at least one of the chosen characters should be 1.
The player who can't make a valid move loses the game. This also means that if the string currently has less than 2
 characters, the current player loses the game.

You are given a binary string s
 of length n
. You have to calculate the number of its substrings such that, if the game is played on that substring and both players make optimal decisions, the first player wins. In other words, calculate the number of pairs (l,r)
 such that 1≤l≤r≤n
 and the first player has a winning strategy on the string slsl+1…sr
.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int):

 
if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(codeforces(n))

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
