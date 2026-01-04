"""
Q1. Generate Tag for Video Caption
Easy
3 pt.
You are given a string caption representing the caption for a video.

The following actions must be performed in order to generate a valid tag for the video:

Combine all words in the string into a single camelCase string prefixed with '#'. A camelCase string is one where the first letter of all words except the first one is capitalized. All characters after the first character in each word must be lowercase.

Remove all characters that are not an English letter, except the first '#'.

Truncate the result to a maximum of 100 characters.

Return the tag after performing the actions on caption.

 

Example 1:

Input: caption = "Leetcode daily streak achieved"

Output: "#leetcodeDailyStreakAchieved"

Explanation:

The first letter for all words except "leetcode" should be capitalized.

Example 2:

Input: caption = "can I Go There"

Output: "#canIGoThere"

Explanation:

The first letter for all words except "can" should be capitalized.

Example 3:

Input: caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"

Output: "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"

Explanation:

Since the first word has length 101, we need to truncate the last two letters from the word.

 

Constraints:

1 <= caption.length <= 150
caption consists only of English letters and ' '.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, caption: str) -> str:
        result = "#"
        ll = len(caption)
        count = 1
        space_flag = 0
        for each in caption:
            if each == " ":
                space_flag = 1
                continue
            count += 1
            
            if result[-1] == "#":
                result += each.lower()
                space_flag = 0
            elif space_flag == 1:
                result += each.upper()
                space_flag = 0
            else:
                result += each.lower()
            if count >= 100:
                break
                
        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
