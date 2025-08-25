"""
68. Text Justification
Hard
Topics
Companies
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
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
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        length = 0

        for word in words:
            ll = len(word)
            if length + ll + len(line) > maxWidth:
                lll = len(line)
                if lll == 1:
                    new_line = line[0]+ " "*(maxWidth-length)
                else:
                    spaces = maxWidth-length
                    gaps = lll - 1
                    spaces_gap = spaces//gaps
                    extra_spaces = spaces%gaps
                    
                    new_line = ""
                    for ii in range(lll-1):
                        new_line += line[ii]
                        spaces = spaces_gap
                        if ii < extra_spaces:
                            spaces += 1
                        new_line += " " * spaces
                    new_line += line[-1]
                result.append(new_line)
                line = [word]
                length = ll
            else:
                line.append(word)
                length += ll

        if len(line) > 0:
            #print(line, length)
            new_line = " ".join(line)
            new_line += " " * (maxWidth-len(new_line))
            result.append(new_line)
        
        return result
    
        ### cursor
        result = []
        current_line = []
        current_length = 0
        
        # Group words into lines
        for word in words:
            # If adding this word exceeds maxWidth, process the current line
            if current_length + len(word) + len(current_line) > maxWidth:
                # Justify the current line
                if len(current_line) == 1:
                    # If only one word, left-justify it
                    justified_line = current_line[0] + ' ' * (maxWidth - current_length)
                else:
                    # Calculate spaces between words
                    spaces_needed = maxWidth - current_length
                    gaps = len(current_line) - 1
                    spaces_per_gap = spaces_needed // gaps
                    extra_spaces = spaces_needed % gaps
                    
                    justified_line = ""
                    for i in range(len(current_line) - 1):
                        justified_line += current_line[i]
                        spaces = spaces_per_gap + (1 if i < extra_spaces else 0)
                        justified_line += ' ' * spaces
                    justified_line += current_line[-1]
                
                result.append(justified_line)
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        # Process the last line (left-justified)
        if current_line:
            last_line = ' '.join(current_line)
            last_line += ' ' * (maxWidth - len(last_line))
            result.append(last_line)
        


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
