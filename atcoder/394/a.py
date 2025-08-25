# -*- coding: utf-8 -*-

"""
A - 22222 / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
100 points

Problem Statement
You are given a string 
S consisting of digits.

Remove all characters from 
S except for 2, and then concatenate the remaining characters in their original order to form a new string.

Constraints
S is a string consisting of digits with length between 
1 and 
100, inclusive.
S contains at least one 2.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(s: str):
    ll = len(s)
    if ll == 0:
      return ""
      
    count = 0
    for each in s:
      if each == "2":
        count += 1
    result = "2"*count

    return result


if __name__ == "__main__":
    s = input()
    print(atcoder(s))
