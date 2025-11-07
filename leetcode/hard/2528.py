"""
2528. Maximize the Minimum Powered City
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

 

Example 1:

Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
Example 2:

Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.
 

Constraints:

n == stations.length
1 <= n <= 105
0 <= stations[i] <= 105
0 <= r <= n - 1
0 <= k <= 109
"""

import string
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, stations: List[int], r: int, k: int) -> int:
        ### step 3, helper function, greedy feasibility check using difference array O(n)
        def can(power, r, k, target):
            n = len(power)
            added = [0] * (n+1)
            current_add = 0
            remaining = k

            for ii in range(n):
                current_add += added[ii]
                effective = power[ii] + current_add

                if effective < target:
                    need = target-effective
                    remaining -= need
                    if remaining < 0:
                        return False
                    
                    current_add += need
                    end = ii + r + r + 1
                    if end < n:
                        added[end] -= need

            return True

        n = len(stations)

        ### step 1, initial power for each city by prefix sum of O(1) range queries
        prefix = [0] * (n+1)
        for ii in range(n):
            prefix[ii+1] = prefix[ii] + stations[ii]
        
        power = [0] * n
        for ii in range(n):
            left = max(0, ii-r)
            right = min(n-1, ii+r)
            power[ii] = prefix[right+1] - prefix[left]

        ### step 2, binary search on result
        low, high = min(power), max(power)+k
        result = low
        while low <= high:
            mid = (low+high) // 2
            if can(power, r, k, mid):
                result = mid
                low = mid+1
            else:
                high = mid-1

        return result
