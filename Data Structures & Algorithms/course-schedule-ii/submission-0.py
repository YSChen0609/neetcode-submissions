"""
Method 1 : DFS
Time: O(V+E)
Space: O(V)
Recursively check if a node is:
1. visited
2. in a path
3. once already in the path, there is a deadlock
"""

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list
        preList = defaultdict(list)
        for crs, pre in prerequisites:
            preList[crs].append(pre)

        # start recursively checking
        res = []
        visited = set() # means alrready put in res, and able to finish (no deadlock from it)
        path = set()

        def dfs(crs):
            if crs in path: return False # deadlock
            if crs in visited: return True

            # add curr node to the path and check its pre
            path.add(crs)
            for pre in preList[crs]:
                if not dfs(pre): return False # a deadlock from this pre
            path.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return res

        
