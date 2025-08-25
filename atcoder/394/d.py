# -*- coding: utf-8 -*-

"""
D - Colorful Bracket Sequence / 
Time Limit: 2 sec / Memory Limit: 1024 MB

×
It is prohibited to use generative AI in ongoing AtCoder contests. Please refer to the following rules for more details.

AtCoder Rules against Generative AI - Version 20241206


Score : 
400 points

Problem Statement
You are given a string 
S consisting of six types of characters: (, ), [, ], <, >.

A string 
T is called a colorful bracket sequence if it satisfies the following condition:

It is possible to turn 
T into an empty string by repeating the following operation any number of times (possibly zero):

If there exists a contiguous substring of 
T that is one of (), [], or <>, choose one such substring and delete it.
If the deleted substring was at the beginning or end of 
T, the remainder becomes the new 
T.
Otherwise, concatenate the part before the deleted substring and the part after the deleted substring, and that becomes the new 
T.
Determine whether 
S is a colorful bracket sequence.

Constraints
S is a string of length between 
1 and 
2×10 
5
 , inclusive.
S consists of (, ), [, ], <, >.

"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def atcoder(s: str):
  q = []
  ll = 0
  for each in s:
    if each in "([<":
      q.append(each)
      ll += 1
    else:
      if each == ")":
        if ll == 0:
          return "No"
        left = q.pop()
        ll -= 1
        if left != "(":
          return "No"
      elif each == "]":
        if ll == 0:
          return "No"
        left = q.pop()
        ll -= 1
        if left != "[":
          return "No"
      elif each == ">":
        if ll == 0:
          return "No"
        left = q.pop()
        ll -= 1
        if left != "<":
          return "No"
          
  if ll > 0:
    return "No"
  return "Yes"
      

if __name__ == "__main__":
  s = input()
  print(atcoder(s))
