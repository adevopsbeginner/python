"""
401. Binary Watch
Easy
Topics
Companies
Hint
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".


Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []


Constraints:

0 <= turnedOn <= 10
"""

import string
from typing import List
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, turnedOn: int) -> List[str]:
        if turnedOn in [9,10]:
            return []
        result = []
        t1 = [[0,0]]
        t2 = []
        for ii in range(1,turnedOn+1):
            print(ii)
            for hour in [1, 2, 4, 8]:
                for each in t1:
                    if each[0] + hour < 12 and hour & each[0] == 0:
                        if [each[0] + hour, each[1]] not in t2:
                            t2.append([each[0] + hour, each[1]])

            for minute in [1, 2, 4, 8, 16, 32]:
                for each in t1:
                    if each[1] + minute < 60 and minute & each[1] == 0:
                        if [each[0], each[1] + minute] not in t2:
                            t2.append([each[0], each[1] + minute])
            t1 = t2
            t2 = []
        for each in t1:
            leading = ""
            if each[1] < 10:
                leading = "0"
            result.append(str(each[0])+":"+leading+str(each[1]))

        return result

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    a = 8
    print(len(app.leetcode(a)))
    # print(app.leetcode(a))
