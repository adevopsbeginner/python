"""

Code
Testcase
Test Result
Test Result
2299. Strong Password Checker II
Easy
Topics
Companies
Hint
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

 

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
 

Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
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
    def leetcode(self, password: str) -> bool:
        ll = len(password)
        if ll < 8:
            return False
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0

        for ii in range(ll):
            each = password[ii]
            if ii > 0:
                if each == password[ii-1]:
                    return False
            if each in "0123456789":
                count_digit = 1
            elif each in "abcdefghijklmnopqrstuvwxyz":
                count_lower = 1
            elif each in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                count_upper = 1
            elif each in "!@#$%^&*()-+":
                count_special = 1
        
        if count_lower + count_upper + count_digit + count_special < 4:
            return False

        return True


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
