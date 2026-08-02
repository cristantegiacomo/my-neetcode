# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
    
        new_head = self.reverseList(head.next)

        if head.next:
            head.next.next = head
            head.next = None
        else:
            return head
        
        return new_head