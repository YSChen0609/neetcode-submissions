# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Since BST, so left < root < right
so we can keep going down the left side, then if that's not enough, we get the right from the very end of the left tree

so recursion.

Actually in-order right?
"""

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []


        def trav(root):

            if len(res) >= k: return res[k-1]
            if not root: return None
            
            left = trav(root.left)
            if left is not None: return left
            res.append(root.val)

            return trav(root.right)

        return trav(root)








