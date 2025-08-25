"""
100284. Valid Word
User Accepted:14287
User Tried:16469
Total Accepted:14931
Total Submissions:47238
Difficulty:Easy
A word is considered valid if:

It contains a minimum of 3 characters.
It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
"""
from typing import List

class Solution:
    def leetcode(self, word: str) -> bool:
        ll = len(word)
        if ll < 3:
          return False

        vowels = 0
        constants = 0
        for each in word:
          print(each)
          if not each.isalnum():
            print(1)
            return False
          if each in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print(2)
            pass
          elif each in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            print(3)
            vowels += 1
          else:
            print(4)
            constants += 1
        return vowels and constants and True
                
if __name__ == "__main__":
    app = Solution()
    a = "234Adas"
    print(app.leetcode(a))