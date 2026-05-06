# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
since subroot is a "smaller" tree
we can:
1. find the node in root with the same val as the root of subtree
2. start from that node and trav down to check if its subtree == subtree
3. Use a bfs (for tree: root) 

time: O(n**2)
space: O(n+n)
"""

from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(root_n) -> bool:
            q = deque([root_n])
            subq = deque([subRoot])
            
            while subq:
                n1, n2 = q.popleft(), subq.popleft()
                if n1 is None and n2 is None: continue
                if n1 is None or n2 is None or n1.val != n2.val: return False
                q.append(n1.left)
                q.append(n1.right)
                subq.append(n2.left)
                subq.append(n2.right)
                
            return (not subq and not q)



        q = deque([root])

        while q:
            node_r = q.popleft()
            if node_r:
                q.append(node_r.left)
                q.append(node_r.right)
                if node_r.val == subRoot.val and isSametree(node_r):
                    # compare two trees
                    print("a!")
                    return True
        
        return False
                 






