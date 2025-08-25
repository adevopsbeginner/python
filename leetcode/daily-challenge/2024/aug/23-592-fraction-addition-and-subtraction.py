"""
592. Fraction Addition and Subtraction
Medium
Topics
Companies
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"


Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.592. Fraction Addition and Subtraction
Medium
Topics
Companies
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"


Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
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
    def leetcode(self, expression: str) -> str:
        ll = 12
        lsign = [1] * ll
        lnume = [0] * ll
        ldeno = [1] * ll

        sign = 1
        nume = 0
        deno = 1
        index = 1
        flag = 0
        for each in expression:
            if each in "-+":
                lsign[index]  = sign
                lnume[index]  = nume
                ldeno[index]  = deno

                if each == "-":
                    sign = -1
                else:
                    sign = 1

                flag = 0
                nume = 0
                deno = 0
                index += 1
            elif each == "/":
                deno = 0
                flag = 1
            elif flag:
                deno = deno*10 + int(each)
            else:
                nume = nume*10 + int(each)
        lsign[index]  = sign
        lnume[index]  = nume
        ldeno[index]  = deno

        print(lsign)
        print(lnume)
        print(ldeno)

        for ii in range(1,ll):
            if lnume[ii] == 0:
                continue
            #print(lsign[0], lnume[0], ldeno[0], lsign[ii], lnume[ii], ldeno[ii])
            lnume[0] = lsign[0]*lnume[0]*ldeno[ii] + lsign[ii]*lnume[ii]*ldeno[0]
            ldeno[0] *= ldeno[ii]
            if lnume[0] >= 0:
                lsign[0] = 1
            else:
                lsign[0] = -1
                lnume[0] = abs(lnume[0])
            print(lsign[0], lnume[0], ldeno[0])
        if lnume[0] == 0:
            return "0/1"
        elif lnume[0] == ldeno[0]:
            lnume[0] = 1
            ldeno[0] = 1
        elif lnume[0] < ldeno[0]:
            n = lnume[0]
            for ii in range(n,1,-1):
                while lnume[0] % ii == 0 and lnume[0] >= ii:
                    if ldeno[0] % ii == 0:
                        lnume[0] //= ii
                        ldeno[0] //= ii
        else:
            n = ldeno[0]
            for ii in range(n,1,-1):
                while ldeno[0] % ii == 0 and ldeno[0] >= ii:
                    print(ii)
                    if lnume[0] % ii == 0:
                        ldeno[0] //= ii
                        lnume[0] //= ii
                    else:
                        break

        result = str(lnume[0]) + "/" + str(ldeno[0])

        if lsign[0] < 0:
            result = "-" + result

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    a = "-1/2+1/2+1/3"
    a = "7/2+2/3-3/4"
    print(app.leetcode(a))
