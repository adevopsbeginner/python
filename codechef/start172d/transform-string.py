"""
Transform String
Chef gives you 2 strings 
A
A and 
B
B. You can perform the following operation on 
A
A as many times as you want.

Remove character 
A
i
A 
i
​
  from the string 
A
A. This has a cost of 
i
i which is the index of the element that you are removing.
Note that cost is always equal to the index in current string and not the original string. Refer to the sample test case for example.

You have to print the minimum cost of transforming 
A
A to 
B
B using the above operation. If it is not possible to transform string 
A
A to 
B
B, print 
−
1
−1.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of 2 lines of input.
The first line of each test case contains string 
A
A.
The next line contains string 
B
B.
Output Format
For each test case, output on a new line the minimum cost of transforming string 
A
A to 
B
B. If it is not possible to transform string 
A
A to string 
B
B using above operation, print 
−
1
−1.

Constraints
1
≤
T
≤
2
⋅
1
0
5
1≤T≤2⋅10 
5
 
1
≤
∣
A
∣
≤
2
⋅
1
0
5
1≤∣A∣≤2⋅10 
5
  (
∣
A
∣
∣A∣ refers to length of string 
A
A)
1
≤
∣
B
∣
≤
2
⋅
1
0
5
1≤∣B∣≤2⋅10 
5
 
The sum of 
∣
A
∣
∣A∣ and 
∣
B
∣
∣B∣ over all test cases won't exceed 
2
⋅
1
0
5
2⋅10 
5
 .
Sample 1:
Input
Output
3
accd
cd
abcd
ed
aaaabbb
aa
2
-1
11
Explanation:
Test Case 1:

Remove 
A
1
A 
1
​
  which is the character a with cost of 
1
1, 
A
A becomes ccd.
Remove 
A
1
A 
1
​
  which is the character c with cost of 1, 
A
A becomes cd which is equal to 
B
B.
Total cost is 
2
2.
Test Case 2:

It is not possible to transform string 
A
A to 
B
B using the operation.
Test Case 3:

Remove 
A
1
A 
1
​
  with cost 1. Now, 
A
A is aaabbb.
Remove 
A
1
A 
1
​
  with cost 1. Now, 
A
A is aabbb.
Remove 
A
3
A 
3
​
  with cost 3. Now, 
A
A is aabb.
Remove 
A
3
A 
3
​
  with cost 3. Now, 
A
A is aab.
Remove 
A
3
A 
3
​
  with cost 3. Now, 
A
A is aa which is equal to 
B
B.
Total cost is 
11
11.
Did you like the problem statement?
More Info
Time limit1 secs
Memory limit1.5 GB
Source Limit50000 Bytes
"""

import string
import heapq
from typing import List
from collections import defaultdict

# cook your dish here
import sys

def solution(a: str, b: str):
    lla = len(a)
    llb = len(b)
    if lla < llb:
        print(-1)
        return
    indexa = 0
    indexb = 0
    while indexb < llb:
        while indexa < lla and a[indexa] != b[indexb]:
            indexa += 1
        indexa += 1
        indexb += 1
        if indexa >= lla and indexb < llb:
            print(-1)
            return
        
    indexa = lla-1
    indexb = llb-1
    result = 0
    while indexb >= 0 and indexa >= 0:
        #print(indexa,indexb,result)
        if a[indexa] == b[indexb]:
            indexa -= 1
            indexb -= 1
        else:
            indexa -= 1
            result += indexb+2
        if indexb >= 0 and indexa < 0:
            print(-1)
            return
    result += indexa+1

    print(result)

if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        stra = sys.stdin.readline().strip()
        strb = sys.stdin.readline().strip()
        solution(stra,strb)

