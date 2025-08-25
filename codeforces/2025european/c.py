# -*- coding: utf-8 -*-

"""
C. Ads
time limit per test3 seconds
memory limit per test1024 megabytes
You have n
 videos on your watchlist on the popular platform YooCube. The i
-th video lasts di
 minutes.

YooCube has recently increased the frequency of their ads. Ads are shown only between videos. After finishing a video, an ad is shown if either of these two conditions is true:

three videos have been watched since the last ad;
at least k
 minutes have passed since the end of the last ad.
You want to watch the n
 videos in your watchlist. Given that you have just watched an ad, and that you can choose the order of the n
 videos, what is the minimum number of ads that you are forced to watch? You can start a new video immediately after the previous video or ad ends, and you don't have to watch any ad after you finish.
"""

import string
import heapq
from typing import List
from collections import defaultdict
import sys

def codeforces(n: int, arr: list):

if __name__ ==  "__main__":
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(codeforces(n,1,a,b))
