'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
class Solution:
    def leetcode(self, strs: List[str]) -> str:
        result = ""
        ll = len(strs)

        if ll == 0:
            return result
        
        astr = strs[0]

        lla = len(astr)

        for ii in range(lla):
            for each in strs:
                if len(each) <= ii:
                    return result
                if astr[ii] != each[ii]:
                    return result

            result += astr[ii]

        return result

if __name__ == "__main__":
    app = Solution()
    print(app.leetcode(["flower","flow","flight"]))
