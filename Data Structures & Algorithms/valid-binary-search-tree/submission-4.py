# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Practice explict stack dfs.
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, -math.inf, math.inf]] # [[node, lo, hi]]

        while stack:
            node, lo, hi = stack.pop()
            if not lo < node.val < hi: return False
            if node.left: stack.append([node.left, lo, node.val])
            if node.right: stack.append([node.right, node.val, hi])
        
        return True





