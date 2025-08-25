"""
2471. Minimum Number of Operations to Sort a Binary Tree by Level
Medium
Topics
Companies
Hint
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All the values of the tree are unique.
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
    def leetcode(self, root: Optional[TreeNode]) -> int:
        def sort_count(arr: []) -> int:
            n = len(arr)
            # Create a list of tuples where each tuple is (element, index)
            sorted_arr = sorted((value, index) for index, value in enumerate(arr))
            
            # Visited array to mark elements already in place
            visited = [False] * n
            swaps = 0

            for i in range(n):
                # If the element is already in the correct position or visited, skip it
                if visited[i] or sorted_arr[i][1] == i:
                    continue
                
                # Find the cycle of misplaced elements
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = sorted_arr[x][1]  # Move to the index where the current element should be
                    cycle_size += 1
                
                # Add (cycle_size - 1) swaps for this cycle
                if cycle_size > 1:
                    swaps += (cycle_size - 1)
            
            return swaps
            ll = len(arr)
            if ll <= 1:
                return 0
            sorted_arr = sorted(arr)
            #print(result, arr)
            #print(result, sorted_arr)
            count = 0
            for ii in range(ll):
                for jj in range(ll):
                    if sorted_arr[ii] == arr[jj]:
                        if ii != jj:
                            arr[ii],arr[jj] = arr[jj],arr[ii]
                            count += 1
            #print(result, count, arr)
            return count

        q = [[root,0]]
        current_level = 0
        this_level = []
        result = 0
        while q:
            p,l = q.pop(0)
            if l > current_level:
                result += sort_count(this_level)
                this_level = [p.val]
            else:
                this_level.append(p.val)

            current_level = l
            if p.left:
                q.append([p.left,l+1])
            if p.right:
                q.append([p.right,l+1])
        
        result += sort_count(this_level)

        return result


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
