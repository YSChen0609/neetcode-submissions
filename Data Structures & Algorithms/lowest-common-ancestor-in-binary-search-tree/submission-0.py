# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
This is a BST!
Use the property of the BST
start from the root, and gradually go down
once encounter a not such as p.val < node.val < q.val, we know node is C.A.
to further get the LCA, keep going down until reaches p or q

time: O(logn)
space: O(1)
"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # make sure p.val < q.val
        if p.val > q.val: p, q = q, p

        cur_node = root
        while True:
            if cur_node.val == p.val: return p
            if cur_node.val == q.val: return q
            # go left
            if p.val < cur_node.val and q.val < cur_node.val: 
                cur_node = cur_node.left
                continue
            # go right
            if p.val > cur_node.val and q.val > cur_node.val: 
                cur_node = cur_node.right
                continue
            # LCA reached
            if p.val < cur_node.val and q.val > cur_node.val: 
                return cur_node



