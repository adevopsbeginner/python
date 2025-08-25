"""
Q2. Assign Elements to Groups with Constraints
Medium
4 pt.
You are given an integer array groups, where groups[i] represents the size of the ith group. You are also given an integer array elements.

Your task is to assign one element to each group based on the following rules:

An element j can be assigned to a group i if groups[i] is divisible by elements[j].
If there are multiple elements that can be assigned, assign the element with the smallest index j.
If no element satisfies the condition for a group, assign -1 to that group.
Return an integer array assigned, where assigned[i] is the index of the element chosen for group i, or -1 if no suitable element exists.

Note: An element may be assigned to more than one group.

 

Example 1:

Input: groups = [8,4,3,2,4], elements = [4,2]

Output: [0,0,-1,1,0]

Explanation:

elements[0] = 4 is assigned to groups 0, 1, and 4.
elements[1] = 2 is assigned to group 3.
Group 2 cannot be assigned any element.
Example 2:

Input: groups = [2,3,5,7], elements = [5,3,3]

Output: [-1,1,0,-1]

Explanation:

elements[1] = 3 is assigned to group 1.
elements[0] = 5 is assigned to group 2.
Groups 0 and 3 cannot be assigned any element.
Example 3:

Input: groups = [10,21,30,41], elements = [2,1]

Output: [0,1,0,1]

Explanation:

elements[0] = 2 is assigned to the groups with even values, and elements[1] = 1 is assigned to the groups with odd values.

 

Constraints:

1 <= groups.length <= 105
1 <= elements.length <= 105
1 <= groups[i] <= 105
1 <= elements[i] <= 105
"""

from typing import List
from collections import defaultdict

class Solution:
    def leetcode(self, groups: List[int], elements: List[int]) -> List[int]:
        index = sorted((ii,e) for ii,e in enumerate(elements))
        llg = len(groups)
        lle = len(elements)
        dd = defaultdict(int)

        for indexe,e in index:
            if e in dd:
                continue
            for m in range(e,max(groups)+1,e):
                if m not in dd:
                    dd[m] = indexe
        result = [dd.get(group, -1) for group in groups]
        return result

        for ii in range(llg):
            for indexe,e in index:
                #print(groups[ii],e,indexe)
                if groups[ii]%e == 0:
                    result[ii] = indexe
                    break
        return result
                    
        
        dd = defaultdict(int)
        ddg = defaultdict(int)
        for ii in range(lle):
            if elements[ii] not in dd:
                dd[elements[ii]] = ii
        
        result = [-1]*llg
        for ii in range(llg):
            if groups[ii] in ddg:
                result[ii] = dd[groups[ii]]
                continue
            for each in dd:
                if groups[ii]%each == 0:
                    result[ii] = dd[each]
                    break
        return result
                
        ### time limit exceeded
        llg = len(groups)
        lle = len(elements)
        result = [-1]*llg
        for jj in range(llg):
            for ii in range(lle):
                if groups[jj]%elements[ii] == 0:
                    result[jj] = ii
                    break
        
        return result©leetcode

if __name__ == "__main__":
    app = Solution()
    a = [1,4,3,3,2]
    b = 2
    print(app.leetcode(a))
