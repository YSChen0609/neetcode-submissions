# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
idea: get the diff-height of each node
recursively
time: O(n)
space: O(1)
"""


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_h(node) -> int:
            if not node: return 0
            l_h, r_h = get_h(node.left), get_h(node.right)
            if l_h is False or r_h is False: return False
            if abs(l_h-r_h) > 1: return False
            return max(l_h, r_h)+1
        
        if get_h(root) is False: return False
        else: return True


        