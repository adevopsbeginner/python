"""
1154. Day of the Year
Easy
Topics
Companies
Hint
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31th, 2019.
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
    def leetcode(self, date: str) -> int:
        day = int(date[8:])
        month = int(date[5:7]) 
        year = int(date[:4])
        result = day
        for ii in range(month):
            days = [0,31,28,31,30,31,30,31,31,30,31,30]
            result += days[ii]

        if year%4 == 0 and (year%100 or year == 2000) > 0 and month > 2:
            result += 1

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
