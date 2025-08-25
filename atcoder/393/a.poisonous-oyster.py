# -*- coding: utf-8 -*-

"""
A - Poisonous Oyster / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
100 points

Problem Statement
There are four types of oysters, labeled 
1, 
2, 
3, and 
4. Exactly one of these types causes stomach trouble if eaten. The other types do not cause stomach trouble when eaten.

Takahashi ate oysters 
1 and 
2, and Aoki ate oysters 
1 and 
3. The information on whether each person got sick is given as two strings 
S 
1
​
  and 
S 
2
​
 . Specifically, 
S 
1
​
 = sick means Takahashi got sick, and 
S 
1
​
 = fine means Takahashi did not get sick. Likewise, 
S 
2
​
 = sick means Aoki got sick, and 
S 
2
​
 = fine means Aoki did not get sick.

Based on the given information, find which type of oyster causes stomach trouble.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(s1: str, s2: str):
    if s1 == "fine" and s2 == "fine":
      return 4
    elif s1 == "fine" and s2 == "sick":
      return 3
    elif s1 == "sick" and s2 == "fine":
      return 2
    elif s1 == "sick" and s2 == "sick":
      return 1

    return 1


if __name__ == "__main__":
    s1, s2 = list(input().split())
    print(atcoder(s1, s2))