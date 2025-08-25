"""

"""

import string
import heapq
from typing import List
from collections import defaultdict

import sys

def solution(n: int, q: int):
  az = []
  for ii in range(n):
    az.append(chr(ii+ord("A")))
  count = 0
  
  matrix = [[0 for _ in range(n)] for _ in range(n)]

  for ii in range(n):
    swapped = 0
    for jj in range(n-ii-1):
      if matrix[jj][jj+1] == 0:
        count += 1
        print("? ", az[jj], az[jj+1])
        answer = sys.stdin.readline().strip()
        if answer[0] == "<":
          matrix[jj][jj+1] = -1
        else:
          matrix[jj][jj+1] = 1

      if matrix[jj][jj+1] == 1:
        az[jj], az[jj+1] = az[jj+1], az[jj]
        swapped = 1

      if swapped == 0:
        break

  result = "! "
  for each in az:
    result += each
  print(result)

if __name__ == "__main__":
  line1 = sys.stdin.readline().strip()
  nq = line1.split(" ")
  n = int(nq[0])
  q = int(nq[1])
  solution(n,q)
