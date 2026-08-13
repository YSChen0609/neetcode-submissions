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
Time: O(k)
Space: O(k)

can further reduce space complexity by using counter not list
Space: O(1)
"""

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        def trav(root):
            if not root: return None
            
            left = trav(root.left)
            if left is not None: return left
            self.cnt += 1
            if self.cnt == k: return root.val

            return trav(root.right)

        return trav(root)








