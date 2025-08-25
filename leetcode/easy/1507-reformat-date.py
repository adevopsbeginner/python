"""
1507. Reformat Date
Solved
Easy
Topics
Companies
Hint
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
 

Example 1:

Input: date = "20th Oct 2052"
Output: "2052-10-20"
Example 2:

Input: date = "6th Jun 1933"
Output: "1933-06-06"
Example 3:

Input: date = "26th May 1960"
Output: "1960-05-26"
 

Constraints:

The given dates are guaranteed to be valid, so no error handling is necessary.
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
    def leetcode(self, date: str) -> str:
        ll = len(date)

        result = date[ll-4:]

        result += "-"        
        month = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        if date[ll-8:ll-5] == "Oct":
            result += "10"
        elif date[ll-8:ll-5] == "Nov":
            result += "11"
        elif date[ll-8:ll-5] == "Dec":
            result += "12"
        else:
            result += "0"
            for ii in range(10):
                if date[ll-8:ll-5] == month[ii]:
                    result += str(ii)

        result += "-"
        if date[1] in "01234567890":
            result += date[:2]
        else:
            result += "0" + date[0]
        
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
