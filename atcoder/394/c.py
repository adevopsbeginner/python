# -*- coding: utf-8 -*-

"""
C - Debug / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
300 points

Problem Statement
You are given a string 
S consisting of uppercase English letters.
Apply the following procedure to 
S, and then output the resulting string:

As long as the string contains WA as a (contiguous) substring, repeat the following operation:

Among all occurrences of WA in the string, replace the leftmost one with AC.
It can be proved under the constraints of this problem that this operation is repeated at most a finite number of times.

Constraints
S is a string of uppercase English letters with length between 1 and 
3×10 
5
 , inclusive.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(s: str):
  slist = list(s)
  ll = len(s)
  ii = 0
  
  while ii < ll-1:
    if slist[ii] == "W" and slist[ii+1] == "A":
      slist[ii], slist[ii+1] = "A", "C"
      ii = max(0, ii-1)
    else:
      ii += 1
  result = "".join(slist)
  return result
  
  ### tle
  while "WA" in s:
    s = s.replace("WA", "AC", 1)
  return s
  
  ### tle
  ll = len(s)
  index = []
  result = ""
  for ii in range(1,ll):
    if s[ii] == "A" and s[ii-1] == "W":
      index.append(ii)
    
  ### tle
  ll = len(s)
  result = ""
  countw = 0
  index = 0
  for ii in range(ll):
    #print("111", result)
    if s[ii] == "W":
      countw += 1
    elif s[ii] == "A":
      if countw > 0:
        result += "A" + "C"*countw
        countw = 0
      else:
        result += "A"
    else:
      if countw > 0:
        result += "W"*countw
        countw = 0
      result += s[ii]
    
  if countw > 0:
    result += "W"*countw

  return result

  ### tle
  q = []
  c = ""
  for each in s:
    if each == "A":
      while len(q) > 0 and q[-1] == "W":
        q.pop()
        c += "C"
      q.append("A"+c)
      c = ""
    else:
      q.append(each)
      
  result = "".join(q)

  return result

  
if __name__ == "__main__":
  s = input()
  print(atcoder(s))
  