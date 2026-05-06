# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# use BFS for both trees
# Time: O(n)
# space: O(n)

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])

        while q1 and q2:
            cur1, cur2 = q1.popleft(), q2.popleft()
            if cur1 and cur2: # they both exist
                if cur1.val != cur2.val: return False
                # update the queues
                q1.append(cur1.left)
                q2.append(cur2.left)
                q1.append(cur1.right)
                q2.append(cur2.right)
                continue
            if not cur1 and not cur2: continue # they both non-exist

            return False # one exists but not the other
        
        return (not q1 and not q2)
            







