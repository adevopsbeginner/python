'''
100294. Count the Number of Special Characters I
User Accepted:5055
User Tried:5829
Total Accepted:5100
Total Submissions:6671
Difficulty:Easy
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

 

Constraints:

1 <= word.length <= 50
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
        for each in 'abcdefghijklmnopqrstuvwxyz':
            if each in word and each.upper() in word:
                #print(each)
                result += 1
                
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,3,5,6]
    a = "aaAbcBC"
    b = "1011"
    print(app.leetcode(a))