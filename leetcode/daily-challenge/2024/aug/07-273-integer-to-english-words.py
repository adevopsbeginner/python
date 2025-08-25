"""
273. Integer to English Words
Solved
Hard
Topics
Companies
Hint
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1
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
    def leetcode(self, num: int) -> str:
        def ten(num10: int) -> str:
            if num10 == 0:
                return ""
            if num10 < 10:
                return read1[num10]
            if num10 < 20:
                return read11[num10-10]
            result10 = read20[num10//10]
            if num10 % 10:
                result10 += " " + read1[num10%10]
            #print(result10 + "x")

            return result10

        def hundred(num100: int) -> str:
            result100 = ""
            if num100 == 0:
                return result100
            if num100 % 100:
                result100 = ten(num100 % 100)
            if num100 > 99:
                if len(result100):
                    result100 = " " + result100
                result100 = read1[num100//100] + " Hundred" + result100

            #print(result100 + "x")

            return result100

        if num == 0:
            return "Zero"

        result = ""
        read = ["", " Thousand", " Million", " Billion"]
        read1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        read11 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        read20 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        numq = num
        for ii in range(4):
            numr = numq % 1000
            numq //= 1000
            if numq == 0 and numr == 0:
                break
            elif numr == 0:
                continue
            else:
                if len(result):
                    result = " " + result
                result = hundred(numr) + read[ii] + result
                #print(result + "x")

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
