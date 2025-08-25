"""
1185. Day of the Week
Easy
Topics
Companies
Hint
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

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
    def leetcode(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        count = 4 ### 1 Jan 1971 is Friday
        count += 365*(year-1971)
        for ii in range(1971,year):
            if ii%400 == 0:
                count += 1
            elif ii%100 == 0:
                pass
            elif ii%4 == 0:
                count += 1
        for ii in range(month):
            month_days = [0,31,28,31,30,31,30,31,31,30,31,30]
            count += month_days[ii]
        if month > 2:
            if year%400 == 0:
                count += 1
            elif year%100 == 0:
                pass
            elif year%4 == 0:
                count += 1
        count += day
        count %= 7

        return days[count]


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
