# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# layer by layer: bfs
# within each layer, I only put the "last" element in res
# time: O(n)
# space: O(n)

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # edge case
        if not root: return []

        res = []
        q = deque([root])

        while q:
            L = len(q)
            for i in range(L):
                cur = q.popleft()
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                # add last element of this layer
                if i == L-1: res.append(cur.val)
            
        return res





