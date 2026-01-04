"""
Q2. Longest Common Prefix Between Adjacent Strings After Removals
Medium
4 pt.
You are given an array of strings words. For each index i in the range [0, words.length - 1], perform the following steps:

Remove the element at index i from the words array.
Compute the length of the longest common prefix among all adjacent pairs in the modified array.
Return an array answer, where answer[i] is the length of the longest common prefix between the adjacent pairs after removing the element at index i. If no adjacent pairs remain or if none share a common prefix, then answer[i] should be 0.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.
 

Example 1:

Input: words = ["jump","run","run","jump","run"]

Output: [3,0,0,3,3]

Explanation:

Removing index 0:
words becomes ["run", "run", "jump", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 1:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 2:
words becomes ["jump", "run", "jump", "run"]
No adjacent pairs share a common prefix (length 0)
Removing index 3:
words becomes ["jump", "run", "run", "run"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Removing index 4:
words becomes ["jump", "run", "run", "jump"]
Longest adjacent pair is ["run", "run"] having a common prefix "run" (length 3)
Example 2:

Input: words = ["dog","racer","car"]

Output: [0,0,0]

Explanation:

Removing any index results in an answer of 0.
 

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 104
words[i] consists of lowercase English letters.
The sum of words[i].length is smaller than or equal 105.
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, words: List[str]) -> List[int]:
        ### time limt exceeded
        def longest_common_prefix(str1, str2):
            ll1 = len(str1)
            ll2 = len(str2)
            ll = min(ll1, ll2)
            for ii in range(ll):
                if str1[0:ii+1] != str2[0:ii+1]:
                    return ii
            return ll

        ll = len(words)
        if ll == 1:
            return [0]
        if ll == 2:
            return [0,0]
            
        forward = [0]*ll
        backward = [0]*ll
        result = [0]*ll
        #forward[0] = longest_common_prefix(words[0], words[1])
        backward[-1] = longest_common_prefix(words[-1], words[-2])
        for ii in range(ll-1):
            lcp = longest_common_prefix(words[ii], words[ii+1])
            forward[ii] = lcp
            forward[ii+1] = lcp
            
        # for ii in range(ll-1):
        #     forward[ii] = longest_common_prefix(words[ii], words[ii+1])
        # for ii in range(1, ll):
        #     backward[ii] = longest_common_prefix(words[ii], words[ii-1])

        #print(forward)
        #print(backward)

        result[0] = max(max(forward[1:]), max(backward[2:]))
        result[-1] = max(max(forward[0:ll-2]), max(backward[0:ll-1]))
        
        for ii in range(1, ll-1):
            before = 0
            if ii-1 > 0:
                before = max(max(forward[0:ii-1]), max(backward[0:ii-1]))
            
            before_after = longest_common_prefix(words[ii-1], words[ii+1])

            after = 0
            after_forward = 0
            if ii+1 < ll-1:
                after_forward = max(forward[ii+1:])
            after_backward = 0
            if ii+2 < ll-1:
                after_backward = max(backward[ii+2:])
            after = max(after_forward, after_backward)
                
            result[ii] = max(before, before_after, after)

        return result

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
