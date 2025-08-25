"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
Solved
Medium
Topics
Companies
Hint
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

 

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 

Constraints:

1 <= n <= 10
1 <= k <= 100
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
    def leetcode(self, n: int, k: int) -> str:
        """
        a ...
         - b
         - c
        b ...
        c ...
        total number = 3*2^(n-1)
        """
        next1 = {"a": "b", "b": "a", "c": "a"}
        next2 = {"a": "c", "b": "c", "c": "b"}
        abc1 = ["a", "b", "c", "c"]

        abc2power = 2**(n-1)
        result = ""
        if k > 3 * abc2power:
            return result
        ### n=1, k=1, result="a"
        elif n == 1:
            return abc1[k-1]
        else:
            index = k//abc2power
            if k%abc2power == 0:
                index -= 1
            result = abc1[index]
        k %= abc2power

        for ii in range(n-1):
            #print(ii,k, n-1-1-ii, (2**(n-1-1-ii)), k % (2**(n-1-1-ii)), next2[result[-1]])
            if k == 0:
                result += next2[result[-1]]
            elif k <= 2**(n-1-1-ii):
                result += next1[result[-1]]
            else:
                result += next2[result[-1]]
            k %= 2**(n-1-1-ii)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
