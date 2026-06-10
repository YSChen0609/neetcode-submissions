# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Do a dfs-like trav, pass the largest node val so far to the next layer

- time: O(n)
- space: O(n)-call stack
"""

class Solution:
    good_cnt = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest_val):
            if not node: return
            if node.val >= largest_val:
                self.good_cnt += 1
                largest_val = max(largest_val, node.val)
            
            dfs(node.left, largest_val)
            dfs(node.right, largest_val)
        
        dfs(root, -101)

        return self.good_cnt









