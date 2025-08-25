"""

Code
Testcase
Test Result
Test Result
819. Most Common Word
Easy
Topics
Companies
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.



Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"


Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
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
    def leetcode(self, paragraph: str, banned: List[str]) -> str:
        ll = len(paragraph)
        start = -1
        end = -1
        llist = []
        for ii in range(ll):
            if paragraph[ii] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if start < 0:
                    start = ii
            else:
                if start >= 0:
                    end = ii
                    llist.append(paragraph[start:end])
                    start = -1
                    end = -1
        if start >= 0:
            llist.append(paragraph[start:])
        #print(llist)

        # llist = paragraph.split(" ")
        dd = defaultdict(int)
        for each in llist:
            # each.lower()
            if each.lower() not in banned:
                dd[each.lower()] += 1
        #print(dd)

        result = ""
        count = 0
        for each in dd:
            if dd[each] > count:
                count = dd[each]
                result = each

        return result

if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
