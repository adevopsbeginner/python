'''
67. Add Binary
Solved
Easy
Topics
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, a: str, b: str) -> str:
        result = ""
        lla = len(a)
        llb = len(b)
        ll = max(lla,llb)
        if ll == 0:
            return "0"
        c = "0"
        if lla > llb:
            b = "0"*(lla-llb)+b
        else:
            a = "0"*(llb-lla)+a

        for ii in range(ll-1,-1,-1):
            addup = a[ii]+b[ii]+c
            print(a,b,c, addup)
            if addup == "000":
                result = "0"+result
                c = "0"
            elif addup == "111":
                result = "1"+result
                c = "1"
            elif addup in ["100", "010", "001"]:
                result = "1"+result
                c = "0"
            else:
                result = "0"+result
                c = "1"
        if c == "1":
            result = c+result
        
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = "1010"
    b = "1011"
    print(app.leetcode(a,b))
