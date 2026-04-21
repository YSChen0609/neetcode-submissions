# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use dfs (stack) to record the longest depth
# time: O(N)
# space: O(N)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # edge case
        if not root: return 0

        dfs_stack = [root]
        visited = set()
        res = 0

        while dfs_stack:
            res = max(res, len(dfs_stack))
            curr = dfs_stack[-1]
            visited.add(curr)

            # add (one of the) child(ren) to the stack
            if curr.left and curr.left not in visited: 
                dfs_stack.append(curr.left)
                continue
            if curr.right and curr.right not in visited: 
                dfs_stack.append(curr.right)
                continue
            
            # leaf node or subtree done visited, return
            if (not curr.left and not curr.right) or (curr in visited): 
                dfs_stack.pop()

        return res



