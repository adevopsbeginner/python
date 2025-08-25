# -*- coding: utf-8 -*-

"""
Assignment Due
You are eagerly awaiting for the upcoming Technex event organized by IIT BHU Varanasi! However, you also have an assignment due. The deadline for the assignment is in 
Y
Y days, and it takes you 
X
X days to complete it.

Determine whether you can finish the assignment on or before the deadline.

Input Format
The input consists of two space-separated integers 
X
X and 
Y
Y, where:

X
X denotes the number of days required to complete the assignment.
Y
Y denotes the number of days remaining until the deadline.
Output Format
Print YES if you can complete the assignment on or before the due date, otherwise print NO

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Constraints
1
≤
X
≤
100
1≤X≤100
1
≤
Y
≤
100
1≤Y≤100
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


def codechef(x: int, y: int):
    if x <= y:
        return "YES"
    return "NO"
    
if __name__ == "__main__":
    x,y = list(map(int, input().split()))
    print(codechef(x,y))
