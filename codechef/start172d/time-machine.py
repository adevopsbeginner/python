"""
Time Machine
Chef is currently in the year 
X
X in Chefland. He has a time machine that allows him to travel at most 
25
25 years into the future, but he can use it only once.

Determine whether Chef can reach the year 
2050
2050 with a single use of the time machine.

Input Format
A single integer 
X
X, representing current year in Chefland.

Output Format
Print YES if Chef can reach the year 2050 , otherwise print NO.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Constraints
2000
≤
X
≤
2050
2000≤X≤2050
"""

import string
import heapq
from typing import List
from collections import defaultdict

# cook your dish here
import sys

def travel():
    ns = sys.stdin.readline().strip()
    n = int(ns)
    if n >= 2025:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    travel()
