"""
443. String Compression
Solved
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
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
    def leetcode(self, chars: List[str]) -> int:
        ll = len(chars)
        chars.append("")
        index = 0
        count = 0
        for ii in range(0,ll+1):
            if chars[ii] == chars[ii-1]:
                count += 1
            else:
                if count > 1:
                    scount = str(count)
                    llscount = len(scount)
                    for jj in range(llscount):
                        chars[index] = scount[jj]
                        index += 1
                chars[index] = chars[ii]
                index += 1
                count = 1

        result = index-1
        
        return result

        ### wrong answer
        index = 0
        dd = defaultdict(int)
        for each in chars:
            dd[each] += 1
        index = 0
        for each in dd:
            if dd[each] == 1:
                chars[index] = each
                index += 1
            else:
                chars[index] = each
                index += 1
                sdd = str(dd[each])
                llsdd = len(sdd)
                for ii in range(llsdd):
                    chars[index] = sdd[ii]
                    index += 1
        return index


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
