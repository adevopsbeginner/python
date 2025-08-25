"""
748. Shortest Completing Word
Easy
Topics
Companies
Hint
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.



Example 1:

Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
Output: "steps"
Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
"step" contains 't' and 'p', but only contains 1 's'.
"steps" contains 't', 'p', and both 's' characters.
"stripe" is missing an 's'.
"stepple" is missing an 's'.
Since "steps" is the only word containing all the letters, that is the answer.
Example 2:

Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
Output: "pest"
Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.


Constraints:

1 <= licensePlate.length <= 7
licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
1 <= words.length <= 1000
1 <= words[i].length <= 15
words[i] consists of lower case English letters.
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
    def leetcode(self, licensePlate: str, words: List[str]) -> str:
        count = 0
        dd = defaultdict(int)
        for each in licensePlate:
            if each in "abcdefghijklmnopqrstuvwxyz":
                dd[each] += 1
                count += 1
            if each in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                dd[each.lower()] += 1
                count += 1

        result = words[-1]
        ddw = defaultdict(int)
        short = 15
        for word in words:
            ll = len(word)
            if ll < count:
                continue
            if ll >= short:
                continue

            flag = 0
            for each in ddw:
                ddw[each] = 0
            for each in word:
                ddw[each] += 1
            for each in dd:
                if dd[each] > ddw[each]:
                    flag = 1
                    break
            if flag == 0:
                short = ll
                result = word

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
