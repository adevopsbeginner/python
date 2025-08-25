"""
726. Number of Atoms
Hard
Topics
Companies
Hint
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.



Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.


Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
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
    def leetcode(self, formula: str) -> str:
        ll = len(formula)
        copy = formula
        while "(" in copy:
            right = 0
            left = 0
            while copy[right] != ")":
                # print(left,right, copy)
                right += 1
            left = right
            while copy[left] != "(":
                left -= 1

            count = 0
            head = copy[:left]
            middle = copy[left + 1:right]
            print(head,middle)

            if right == ll - 1:
                count = 1
                tail = ""
            elif copy[right + 1] not in "1234567890":
                tail = copy[right + 1:]
            else:
                right += 1
                if right == ll:
                    break
                while copy[right] in "1234567890":
                    count *= 10
                    count += int(copy[right])
                    right += 1
                    if right == ll:
                        break

                if right == ll:
                    tail = ""
                else:
                    tail = copy[right:]

            copy = head
            if count < 1:
                count = 1
            for ii in range(count):
                copy += middle
            copy += tail

        print(copy)

        lcopy = []
        upper_name = ""
        count = -1
        for ii in range(len(copy)-1,-1,-1):
            each = copy[ii]
            if each.isupper():
                if count == -1:
                    count = 1
                lcopy.append([each+upper_name,count])
                upper_name = ""
                count = -1
            elif each.islower():
                if count == -1:
                    count = 1
                upper_name = each + upper_name
            else:
                if count == -1:
                    count = int(each)
                else:
                    count = int(each)*10+count

        print(lcopy)
        dd = defaultdict(int)
        for each in lcopy:
            dd[each[0]] += each[1]
        ld = []
        for each in dd:
            ld.append([each,dd[each]])
        ld.sort()
        print(ld)
        result = ""
        for each in ld:
            result += each[0]
            if each[1] > 1:
                result += str(each[1])


        return result


if __name__ == "__main__":
    app = Solution()
    a = "K4(ON(SO3)2)2"
    a = "H50"
    a = "((HHe28Be26He)9)34"
    a = "Mg(H2O)N"
    print(app.leetcode(a))
