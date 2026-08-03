# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        res = curr = head
        count, i = 0, 1
        while curr:
            count += 1
            curr = curr.next

        prev, curr = None, head
        while curr:
            if i == count-n+1:
                if prev:
                    prev.next = curr.next
                elif curr:
                    head = head.next

            prev = curr
            curr = curr.next
            i += 1
        return head


 #   [1,2]

