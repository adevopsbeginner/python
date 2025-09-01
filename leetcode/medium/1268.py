"""
1268. Search Suggestions System
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
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
    def leetcode(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        llp = len(products)
        lls = len(searchWord)
        result = []
        index = 0
        for ii in range(lls):
            current = []
            while index < llp and (len(products[index]) < ii+1 or searchWord[0:ii+1] != products[index][0:ii+1]):
                index += 1
            if index < llp:
                if len(products[index]) >= ii+1 and searchWord[0:ii+1] == products[index][0:ii+1]:
                    current.append(products[index])
                if index+1 < llp and len(products[index+1]) >= ii+1 and searchWord[0:ii+1] == products[index+1][0:ii+1]:
                    current.append(products[index+1])
                if index+2 < llp and len(products[index+2]) >= ii+1 and searchWord[0:ii+1] == products[index+2][0:ii+1]:
                    current.append(products[index+2])
            result.append(current)
        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
