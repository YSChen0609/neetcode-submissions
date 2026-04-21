# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# use dfs-like
# recursively
# given a node, return its left deepest and right deepest, +1 will be the dia of the subtree
# note that the left deepest of a node = max(deepest LHS of node.left, deepest RHS of node.right)+1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def trav(node) -> int: 
            """
            In the func, update the diameter, return the maxDepth
            """
            if not node: return 0
            max_left, max_right = trav(node.left), trav(node.right)
            self.res = max(self.res, max_left + max_right)

            return max(max_left, max_right)+1

        trav(root)
        return self.res










