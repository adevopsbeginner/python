"""
564. Find the Closest Palindrome
Attempted
Hard
Topics
Companies
Hint
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.



Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.


Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
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
    def leetcode(self, n: str) -> str:
        ### chatgpt
        length = len(n)
        num = int(n)

        # Edge cases: numbers like 999, 1000
        candidates = [
            str(10 ** length + 1),  # Case like 999 -> 1001
            str(10 ** (length - 1) - 1)  # Case like 1000 -> 999
        ]

        # Generating palindromes based on the prefix
        prefix = int(n[:(length + 1) // 2])

        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                candidate = p + p[::-1]
            else:
                candidate = p + p[-2::-1]
            candidates.append(candidate)

        # Convert all candidates to integers and exclude n itself
        candidates = [int(c) for c in candidates if int(c) != num]

        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(x - num), x))

        return str(closest)

        ### chatgpt version 1 failed
        def is_palindrome(x):
            return x == x[::-1]

        def create_palindrome(s):
            """ Generate a palindrome by mirroring the first half to the second. """
            length = len(s)
            if length % 2 == 0:
                return s[:length // 2] + s[:length // 2][::-1]
            else:
                return s[:length // 2 + 1] + s[:length // 2][::-1]

        length = len(n)
        num = int(n)

        # Edge cases: numbers close to the boundaries like 999, 1000
        candidates = [
            str(10**length + 1),  # Case like 999 -> 1001
            str(10**(length-1) - 1)  # Case like 1000 -> 999
        ]

        # Middle candidate by creating palindromes based on the first half of n
        prefix = n[:(length + 1) // 2]
        prefix_int = int(prefix)

        for i in [-1, 0, 1]:
            candidate = create_palindrome(str(prefix_int + i))
            candidates.append(candidate)

        # Convert all candidates to integers
        candidates = list(map(int, candidates))

        # Exclude the number itself
        candidates = [c for c in candidates if c != num]

        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(x - num), x))

        return str(closest)

        ll = len(n)
        if ll == 1:
            return str(int(n)-1)
        if n == "9" * ll:
            return "1" + "0" * (ll-1) + "1"
        if n == "1" + "0" * (ll-1):
            return "9" * (ll-1)
        if n == "1" + "0" * (ll-2) + "1":
            return "9" * (ll-1)

        ln = list(n)
        #print(ln)
        ispalindrome = 1
        ll2 = ll//2
        for ii in range(ll2):
            i1 = ll2-ii-1
            i2 = ll-1-i1
            if ln[i1] != ln[i2]:
                ispalindrome = 0
                ln[i2] = ln[i1]

        if ispalindrome == 0:
            return "".join(ln)

        if ll%2 == 1 and ln[ll2] == "0":
            ln[ll2] = "1"
            return "".join(ln)

        for ii in range(ll2):
            if ln[ll2-ii] != "0":
                ln[ll2-ii] = str(int(ln[ll2-ii])-1)
                if ll%2 == 0:
                    ln[ll2-ii-1] = ln[ll2-ii]
                return "".join(ln)
            else:
                ln[ll2-ii] = "9"
                if ll%2 == 0:
                    ln[ll2-ii-1] = ln[ll2-ii]

        return "".join(ln)


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
