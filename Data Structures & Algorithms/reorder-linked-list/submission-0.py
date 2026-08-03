# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        count = 0
        i = 1

        while curr:
            count += 1
            curr = curr.next

        prev, curr = None, head
        while curr:
            if i > count // 2:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            else:
                curr = curr.next
            i += 1
        
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = tmp
            curr = curr.next