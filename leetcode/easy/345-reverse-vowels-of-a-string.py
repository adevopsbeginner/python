"""

Code
Testcase
Test Result
Test Result
345. Reverse Vowels of a String
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
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
    def leetcode(self, s: str) -> str:
        ll = len(s)
        head = 0
        tail = ll-1
        result = ['-']*ll
        while head <= tail:
            # print(head,tail)
            if head == tail:
                result[head] = s[head]
                break

            if s[head] in ['a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U'] and s[tail] in ['a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result[head] = s[tail]
                result[tail] = s[head]
                head += 1
                tail -= 1
                # print(head,tail,result)
                continue

            if s[tail] in ['a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result[head] = s[head]
                head += 1
            elif s[head] in ['a','e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result[tail] = s[tail]
                tail -= 1
            else:
                result[head] = s[head]
                head += 1
                result[tail] = s[tail]
                tail -= 1
            # print(head,tail,result)

        return ('').join(result)

### solution#2
class Solution:
    def reverseVowels(self, s: str) -> str:
        q = []
        result = ""
        for each in s:
            if each in "aeiouAEIOU":
                q.append(each)
        for each in s:
            if each in "aeiouAEIOU":
                result += q.pop()
            else:
                result += each
        return result

if __name__ == "__main__":
    app = Solution()
    a = "hello"
    a = " "
    print(app.leetcode(a))
