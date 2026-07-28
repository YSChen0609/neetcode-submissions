# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Use the property of BST, the "split on node(root)
So at each root( different lv ), we determine the case:
1. (p or q == root) or (p < root < q) => root is the LCA
2. p and q < root => go down the left child
3. p and q > root => go down the right child
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val: root = root.left
            elif p.val > root.val and q.val > root.val: root = root.right
            else: return root
        
        return None




