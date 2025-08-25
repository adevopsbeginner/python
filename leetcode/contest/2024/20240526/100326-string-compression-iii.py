'''
100326. String Compression III
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.

 

 

Example 1:

Input: word = "abcde"

Output: "1a1b1c1d1e"

Explanation:

Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.

For each prefix, append "1" followed by the character to comp.

Example 2:

Input: word = "aaaaaaaaaaaaaabb"

Output: "9a5a2b"

Explanation:

Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.

For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.
 

Constraints:

1 <= word.length <= 2 * 105
word consists only of lowercase English letters.
'''
from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, word: str) -> str:
        comp = ""
        c = "0"
        count = 0
        for each in word:
            print(each,c,count)
            if each == c:
                count += 1
            else:
                if count > 0:
                    comp += str(count)+c
                c = each
                count = 1

            if count == 9:
                comp += str(count)+c
                count = 0
                c = "0"
        if count > 0:
            comp += str(count)+c

        return comp

if __name__ == "__main__":
    app = Solution()
    a = "abcde"
    a = "aaaaaaaaaaaaaabb"
    b = 2
    print(app.leetcode(a))
