# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Use the 2-ptr technique, with the L and R ptrs having a diff of n
DUMMY,1,2,3,4, NULL
     , ,l, , , r
Since the head may be removed, to avoid tandrum, we assign a dummy node at the beginning
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        l, r = dummy, dummy
        for _ in range(n+1): r = r.next

        # locate the node to remove (next of l)
        while r: 
            l, r = l.next, r.next
        
        # remove the l.next
        print(l.val)
        l.next = l.next.next

        # return the list
        return dummy.next
        


        



