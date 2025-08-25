"""
2976. Minimum Cost to Convert String I
Medium
Topics
Companies
Hint
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].



Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.


Constraints:

1 <= source.length == target.length <= 105
source, target consist of lowercase English letters.
1 <= cost.length == original.length == changed.length <= 2000
original[i], changed[i] are lowercase English letters.
1 <= cost[i] <= 106
original[i] != changed[i]
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
    def leetcode(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        llocc = len(original)
        llst = len(source)
        result = 0
        rows = 26
        matrix = [[-1 for ii in range(rows)] for jj in range(rows)]
        for ii in range(rows):
            matrix[ii][ii] = 0
        for ii in range(llocc):
            if matrix[ord(original[ii])-ord("a")][ord(changed[ii])-ord("a")] > 0:
                matrix[ord(original[ii])-ord("a")][ord(changed[ii])-ord("a")] = min(cost[ii], matrix[ord(original[ii])-ord("a")][ord(changed[ii])-ord("a")])
            else:
                matrix[ord(original[ii])-ord("a")][ord(changed[ii])-ord("a")] = cost[ii]

        for kk in range(rows):
            for ii in range(rows):
                for jj in range(rows):
                    if matrix[ii][kk] >= 0 and matrix[kk][jj] >= 0:
                        if matrix[ii][jj] < 0:
                            matrix[ii][jj] = matrix[ii][kk] + matrix[kk][jj]
                        else:
                            matrix[ii][jj] = min(matrix[ii][kk] + matrix[kk][jj], matrix[ii][jj])
        # for ii in range(rows):
        #     print(matrix[ii])

        for ii in range(llst):
            distance = matrix[ord(source[ii])-ord("a")][ord(target[ii])-ord("a")]
            if distance == -1:
                print(matrix[ord(source[ii])-ord("a")], source[ii], target[ii])
                return -1
            result += distance
        return result


        ### wrong solution because not lowest cost
        dd = defaultdict(int)
        for ii in range(ll):
            if dd[original[ii]+changed[ii]] > 0:
                dd[original[ii],changed[ii]] = min(cost[ii],dd[[original[ii],changed[ii]]])
            else:
                dd[original[ii]+changed[ii]] = cost[ii]
        for each in dd:
            print(each,dd[each])

        for ii in range(llst):
            if source[ii] == target[ii]:
                continue
            if dd[source[ii]+target[ii]] == 0:
                print(source[ii], target[ii])
                return -1
            result += dd[source[ii]+target[ii]]

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    source ="abadcdadac"
    target ="baddbccdac"
    original =["d","c","d","c","b","a"]
    changed =["b" ,"b","c","a","d","d"]
    cost =[8,5,9,1,10,2]
    print(app.leetcode(source,target,original,changed,cost))
