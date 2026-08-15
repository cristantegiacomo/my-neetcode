# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = 0  
        
        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val, counter, l))
                counter += 1    # oppure counter -= 1 basta che ogni nodo abbia un counter diverso
        
        dummy = curr = ListNode(0)
        
        while minHeap:
            val, _, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next