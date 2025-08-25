'''
125. Valid Palindrome
Easy
Topics
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leetcode(self, s: str) -> bool:
        ll = len(s)
        iforward = 0
        ibackward = ll-1
        while iforward < ibackward:
            while iforward < ll:
                if s[iforward].isalnum():
                    break
                iforward += 1
            if iforward >= ibackward:
                break
            while ibackward >= 0:
                if s[ibackward].isalnum():
                    break
                ibackward -= 1
            if iforward >= ibackward:
                break
            if s[iforward].lower() != s[ibackward].lower():
                return False
            if iforward + 1 == ibackward:
                break
            iforward += 1
            ibackward -= 1

        return True

if __name__ == "__main__":
    app = Solution()
    a = "A man, a plan, a canal, : Panama"
    a = ".,"
    a = "0P"
    print(app.leetcode(a))
