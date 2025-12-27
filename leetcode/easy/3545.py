"""
3545. Minimum Deletions for At Most K Distinct Characters
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters, and an integer k.

Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters in the resulting string is at most k.

Return the minimum number of deletions required to achieve this.

 

Example 1:

Input: s = "abc", k = 2

Output: 1

Explanation:

s has three distinct characters: 'a', 'b' and 'c', each with a frequency of 1.
Since we can have at most k = 2 distinct characters, remove all occurrences of any one character from the string.
For example, removing all occurrences of 'c' results in at most k distinct characters. Thus, the answer is 1.
Example 2:

Input: s = "aabb", k = 2

Output: 0

Explanation:

s has two distinct characters ('a' and 'b') with frequencies of 2 and 2, respectively.
Since we can have at most k = 2 distinct characters, no deletions are required. Thus, the answer is 0.
Example 3:

Input: s = "yyyzz", k = 1

Output: 2

Explanation:

s has two distinct characters ('y' and 'z') with frequencies of 3 and 2, respectively.
Since we can have at most k = 1 distinct character, remove all occurrences of any one character from the string.
Removing all 'z' results in at most k distinct characters. Thus, the answer is 2.
 

Constraints:

1 <= s.length <= 16
1 <= k <= 16
s consists only of lowercase English letters.
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
    def leetcode(self, s: str, k: int) -> int:
        dd = defaultdict(int)
        for each in s:
            dd[each] += 1
        lists = list(dd.values())
        lists.sort()
        ll = len(lists)
        if ll <= k:
            return 0
        #print(lists)
        return sum(lists[0:ll-k])

        ### wrong answer
        count = 0
        dd = defaultdict(int)
        for each in s:
            dd[each] += 1
        for each in dd:
            if dd[each] == 1:
                count += 1
        if count > k:
            return count-k
        return 0


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
