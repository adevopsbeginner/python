'''
100291. Count the Number of Special Characters II
User Accepted:785
User Tried:1258
Total Accepted:785
Total Submissions:1407
Difficulty:Medium
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
'''
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def leetcode(self, word: str) -> int:
        result = 0
        ccl = [0]*26
        ccu = [0]*26
        for each  in word:
            ordeach = ord(each)
            if each >= 'a' and each <= 'z':
                index = ordeach-ord('a')
                #print("lower",each, index)
                if ccu[index]:
                    ccl[index] = 0
                else:
                    ccl[index] = 1
                
            if each >= 'A' and each <= 'Z':
                index = ordeach-ord('A')
                #print("upper",each,index)
                ccu[index] = 1

        for ii in range(26):
            result += ccl[ii] * ccu[ii]

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = "aaAbcBC"
    a = "AbBCab"
    b = "1011"
    print(app.leetcode(a))