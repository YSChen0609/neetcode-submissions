# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
To make sure all nodes in the subtree satisfies:
    if in left subtree, val < root
    else: val > root

we use a range for checking validity, i.e., the values should be within the range (lb, ub)

if so, we can do a dfs-like recursion trav

Time: O(n)
Space: O(n)-call stack
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rangecheck(node: Optional[TreeNode], bounds: List[List]) -> bool:
            if not node: return True

            if not bounds[0] < node.val < bounds[1]: return False

            return rangecheck(node.left, [bounds[0], node.val]) and rangecheck(node.right, [node.val, bounds[1]])

        return rangecheck(root, [-math.inf, math.inf])












        