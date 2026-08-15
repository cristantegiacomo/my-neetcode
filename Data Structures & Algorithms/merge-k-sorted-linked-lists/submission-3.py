# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        dummy = curr = ListNode(0)
        minHeap = []

        for l in lists:
            if l:
                heapq.heappush(minHeap, NodeWrapper(l))


        while minHeap:
            node_wrap = heapq.heappop(minHeap)
            curr.next = node_wrap.node
            curr = curr.next

            if node_wrap.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrap.node.next))
        
        return dummy.next