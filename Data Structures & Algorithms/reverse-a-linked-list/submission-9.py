# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            nuova_testa = self.reverseList(head.next)
        
            head.next.next = head
        
            head.next = None
        
            return nuova_testa
        return head