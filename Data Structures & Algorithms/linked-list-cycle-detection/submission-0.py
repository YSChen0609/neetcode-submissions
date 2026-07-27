# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Use Totoise and Hare Algo.
Time: O(n)
Space: O(1)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slo, fast = head, head
        
        # check the fast is enough since if there is an "exit", fast will reach it first
        while fast and fast.next:
            slo = slo.next
            fast = fast.next.next
            if slo == fast:
                return True
        
        return False



