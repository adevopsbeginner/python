"""
1360. Number of Days Between Two Dates
Easy
Topics
Companies
Hint
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

import string
import heapq
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, date1: str, date2: str) -> int:
        def days_from_1971(year: int, month: int, day: int) -> int:
            result = 0
            for y in range(1971,year):
                result += 365
                if y in leapyears:
                    result += 1
            for m in range(1,month):
                result += month_days[m]
                if year in leapyears and m == 2:
                    result += 1
            result += day

            return result

        year1 = int(date1[:4])
        month1 = int(date1[5:7])
        day1 = int(date1[8:])
        year2 = int(date2[:4])
        month2 = int(date2[5:7])
        day2 = int(date2[8:])
        leapyears = [1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]
        month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

        days1 = days_from_1971(year1,month1,day1)
        days2 = days_from_1971(year2,month2,day2)
        print(days1,days2)

        return abs(days1 - days2)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
