'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
  def solution(self, s: str) -> bool:
    q = []
    lr = {")":"(", "]":"[", "}":"{"}
    for each in s:
      if each in "([{":
        q.append(each)
      elif each in ")]}":
        if len(q) == 0:
          return False
        if q[-1] != lr[each]:
          return False
        q.pop() 
    
    if len(q) > 0:
      return False
    return True
  
if __name__ == "__main__":
   app = Solution()
   print(app.solution("()[]{}}"))
