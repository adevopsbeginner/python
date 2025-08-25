"""

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
    def leetcode(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build graph and track in-degrees and out-degrees
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Step 2: Find starting node for Eulerian path
        start_node = None
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break
        
        # If no such node is found, start from any node with edges
        if start_node is None:
            start_node = pairs[0][0]
        
        # Step 3: Hierholzer's algorithm for Eulerian path
        stack = [start_node]
        path = []
        
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            path.append(stack.pop())
        
        # Step 4: Reverse the path to get the correct order
        path.reverse()
        
        # Step 5: Reconstruct valid arrangement
        arrangement = [[path[i], path[i+1]] for i in range(len(path) - 1)]
        return arrangement

        ## my own wrong answer
        ll = len(pairs)
        ddi = defaultdict(int)
        ddl = defaultdict(list)
        for x,y in pairs:
            ddi[x] += 1
            ddi[y] += 1
            ddl[x].append(y)

        first = -1
        last = -1
        for each in ddi:
            if ddi[each]%2 == 1:
                if first == -1 and len(ddl[each]) > 0:
                    first = each
                else:
                    last = each
                if first > 0 and last > 0:
                    break

        index = 0
        print(ll,index, first, ddl[first], last, ddl[last])
        if first > 0 and len(ddl[first]) > 0:
            pairs[0][0] = first
            y = ddl[first].pop(0)
            pairs[0][1] = y
        else:
            ddl[pairs[0][0]].pop(0)

        index = 1
        while index < ll:
            x = pairs[index-1][1]
            pairs[index][0] = x
            print(index,x,ddl[x],pairs)
            y = ddl[x].pop(0)
            pairs[index][1] = y
            index += 1

        # if first > 0:
        #     while dd[first]:
        #         pairs[index//2][index%2] = first
        #         dd[first].pop(0)
        #         index += 1

        # for each in dd:
        #     if dd[each]%2 == 0:
        #         while dd[each] > 0:
        #             pairs[index//2][index%2] = each
        #             dd[each] -= 1
        #             index += 1
            
        # if last > 0:
        #     while dd[last] > 0:
        #         pairs[index//2][index%2] = last
        #         dd[last] -= 1
        #         index += 1

        return pairs


if __name__ == "__main__":
    app = Solution()
    a = [4,5,0,2,3,1]
    print(app.leetcode(a))
