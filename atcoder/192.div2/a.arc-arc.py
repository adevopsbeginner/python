# -*- coding: utf-8 -*-

"""
A - ARC Arc  / 
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 
400 points

Problem Statement
You are given a positive integer 
N and a sequence 
A=(A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 ) of length 
N, consisting of 
0 and 
1.

We call a string 
S of length 
N, consisting only of uppercase English letters, a good string if it is possible to perform the following operation any number of times (possibly zero) so that the sequence 
A contains no 
0. Here, 
S 
i
​
  
(1≤i≤N) denotes the 
i-th character of 
S, and we define 
S 
N+1
​
 =S 
1
​
 , 
S 
N+2
​
 =S 
2
​
 , and 
A 
N+1
​
 =A 
1
​
 .

Perform one of the following operations:
Choose an integer 
i with 
1≤i≤N such that 
S 
i
​
 = A, 
S 
i+1
​
 = R, and 
S 
i+2
​
 = C, and replace each of 
A 
i
​
  and 
A 
i+1
​
  with 
1.
Choose an integer 
i with 
1≤i≤N such that 
S 
i+2
​
 = A, 
S 
i+1
​
 = R, and 
S 
i
​
 = C, and replace each of 
A 
i
​
  and 
A 
i+1
​
  with 
1.
Determine whether there exists a good string.

Constraints
3≤N≤200000
A 
i
​
 ∈{0,1} 
(1≤i≤N)
All input values are integers.
Input
The input is given from Standard Input in the following format:

N
A 
1
​
  
A 
2
​
  
… 
A 
N
​
 
Output
If there exists a good string, print Yes; otherwise, print No.

The judge is case-insensitive; for example, if the correct answer is Yes, outputs such as yes, YES, or yEs will also be accepted.

Sample Input 1
Copy
12
0 1 0 1 1 1 1 0 1 1 1 0
Sample Output 1
Copy
Yes
For example, RARCARCCRAGC is a good string. This is because it is possible to change all elements of 
A to 
1 by performing the following operations:

Initially, 
A=(0,1,0,1,1,1,1,0,1,1,1,0).
Perform the first operation with 
i=2. Then, 
A=(0,1,1,1,1,1,1,0,1,1,1,0).
Perform the first operation with 
i=5. Then, 
A=(0,1,1,1,1,1,1,0,1,1,1,0).
Perform the second operation with 
i=8. Then, 
A=(0,1,1,1,1,1,1,1,1,1,1,0).
Perform the second operation with 
i=12. Then, 
A=(1,1,1,1,1,1,1,1,1,1,1,1).
Since there exists a good string, output Yes.

Sample Input 2
Copy
3
0 0 0
Sample Output 2
Copy
No
Good strings do not exist.

Sample Input 3
Copy
29
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
Sample Output 3
Copy
Yes
Since 
A already contains no 
0, every string of length 
29 consisting of uppercase English letters is a good string.
"""

# -*- coding: utf-8 -*-

import sys

def atcoder(n: int, arr: []):
  if all(arr):
    return "Yes"
  if n%4 == 0:
    return "yes"
  if n%2 == 1:
    if sum(arr) > 0:
      return "yes"
    else:
      return "no"
  odd = 0
  even = 0
  for ii in range(n):
    if arr[ii] == 1:
      if ii%2 == 1:
        odd = 1
      else:
        even = 1
  if odd and even:
    return "yes"
  return "no"

if __name__ == "__main__":
  n = int(input())
  #line2 = sys.stdin.readline().strip()
  arr = list(map(int, input().split()))
  print(atcoder(n, arr))
