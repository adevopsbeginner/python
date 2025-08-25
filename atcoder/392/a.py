# -*- coding: utf-8 -*-

#a = int(raw_input())
# get two integers separated with half-width break
#b, c = map(int, raw_input().split())
# get a string
#s = raw_input()
# output
#print str(a+b+c) + " " + s

import sys

def solution(a: int, b: int, c: int, s: str):
  print(a+b+c, " ", s)

if __name__ == "__main__":
  line1 = sys.stdin.readline().strip()
  a = int(line1)
  line2 = sys.stdin.readline().strip()
  bc = line2.split(" ")
  b = int(bc[0])
  c = int(bc[1])
  line3 = sys.stdin.readline().strip()
  solution(a,b,c,line3)
