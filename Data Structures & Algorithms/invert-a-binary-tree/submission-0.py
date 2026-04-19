# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# use recursion method
# self.right, slef.left = self.left, self.right
# time: O(n)
# space: O(1)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node: return # terminate
            node.right, node.left = invert(node.left), invert(node.right)
            return node
        
        root = invert(root)

        return root





