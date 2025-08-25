# -*- coding: utf-8 -*-

"""
Too Much Homework!
Chef just realized he has a ton of homework due tomorrow!

Chef has several worksheets of questions with him. Each worksheet has exactly 
Y
Y questions in it.
Chef only has the time to complete at most 
10
10 worksheets before the submission deadline.

Chef has previously answered 
X
X questions, and he needs to answer at least 
100
100 questions in total to get a full score for the homework.
Will Chef be able to get a full score?

Input Format
The only line of input will contain two space-separated integers 
X
X and 
Y
Y — the number of questions already answered by Chef, and the number of questions in each worksheet.
Output Format
For each test case, output the answer: "YES" (without quotes) if Chef can receive a full score for the homework, and "NO" (without quotes) otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings No, NO, nO, and no will be treated as equivalent.

Constraints
0
≤
X
≤
150
0≤X≤150
1
≤
Y
≤
10
1≤Y≤10
Sample 1:
Input
Output
73 4
Yes
Explanation:
Chef has already completed 
X
=
73
X=73 questions.
Each worksheet has 
4
4 questions. Chef can complete 
7
7 of them for 
4
⋅
7
=
28
4⋅7=28 questions, which when added to the initial 
73
73 puts him at 
101
101 which is more than 
100
100.

Sample 2:
Input
Output
0 10
Yes
Explanation:
Chef has already completed 
X
=
0
X=0 questions.
Each worksheet has 
10
10 questions. Chef can complete 
10
10 of them for 
10
⋅
10
=
100
10⋅10=100 questions, which when added to the initial 
0
0 puts him at 
100
100 which is enough.

Sample 3:
Input
Output
47 5
No
Explanation:
Chef has already completed 
X
=
47
X=47 questions.
Each worksheet has 
5
5 questions. Even if Chef completes 
10
10 of them for 
10
⋅
5
=
50
10⋅5=50 questions, he will have a total of 
47
+
50
=
97
47+50=97 done which is not enough.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys


# cook your dish here
def codechef(x: int, y: int):
    if x+y*10 >= 100:
        return "YES"
    return "NO"
    
if __name__ == "__main__":
    x,y = list(map(int, input().split()))
    print(codechef(x,y))

    # t = int(sys.stdin.readline().strip())
    # for _ in range(t):
    #     stra = sys.stdin.readline().strip()
    #     strb = sys.stdin.readline().strip()
    #     codechef(stra,strb)
