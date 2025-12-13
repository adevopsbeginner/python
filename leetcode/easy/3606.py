"""
3606. Coupon Code Validator
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order: "electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending) order within each category.

 

Example 1:

Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

First coupon is valid.
Second coupon has empty code (invalid).
Third coupon is valid.
Fourth coupon has special character @ (invalid).
Example 2:

Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

First coupon is inactive (invalid).
Second coupon is valid.
Third coupon has invalid business line (invalid).
 

Constraints:

n == code.length == businessLine.length == isActive.length
1 <= n <= 100
0 <= code[i].length, businessLine[i].length <= 100
code[i] and businessLine[i] consist of printable ASCII characters.
isActive[i] is either true or false.
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
    def leetcode(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ll = len(code)
        combo = []
        for ii in range(ll):
            if len(code[ii]) == 0:
                continue
            if businessLine[ii] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                continue
            if isActive[ii]:
                llc = len(code[ii])
                flag = True
                for jj in range(llc):
                    if code[ii][jj] not in "01234567890_" \
                        and code[ii][jj] not in "abcdefghijklmnopqrstuvwxyz" \
                        and code[ii][jj] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        flag = False
                        break
                if flag:
                    combo.append([businessLine[ii], code[ii]])
        combo.sort()
        result = [combo[ii][1] for ii in range(len(combo))]
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
