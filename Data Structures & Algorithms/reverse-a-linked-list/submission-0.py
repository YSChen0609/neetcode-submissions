# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
0     ->     1    ->    2 -> 3
prev        curr
Idea: use pointers to capture the sub-chain we want to reverse and do it iteratively.
prev, curr = NULL, head # init

curr.next, curr, prev = prev, curr.next, curr
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            curr.next, curr, prev = prev, curr.next, curr
        return prev # the final new head
            





