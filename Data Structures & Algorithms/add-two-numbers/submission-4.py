# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = l1, l2
        mp = defaultdict(int) # nodo -> riporto
        res = prev = None

        while curr1 and curr2:
            rip = 0
            sum = curr1.val + curr2.val
            if sum >= 10:
                sum -= 10 
                rip += 1
            new_node = ListNode(sum) 
            mp[new_node] += rip
            curr1, curr2 = curr1.next, curr2.next

        while curr1:
            mp[ListNode(curr1.val)] = 0
            curr1 = curr1.next
        while curr2:
            mp[ListNode(curr2.val)] = 0 
            curr2 = curr2.next


        for nd in mp:
            if not res: res = nd
            if prev:
                prev.next = nd
                nd.val += mp[prev]
                if nd.val >= 10:
                    nd.val -= 10
                    mp[nd] += 1
            prev = nd

        if prev and mp[prev] > 0:
            new_node = ListNode(1, next=None)
            prev.next = new_node
        
        return res


#   391+
#   654=
#   945
#  1045 


#  9999999+
#     9999=
# 10009998


"""        while curr1 and curr2:
            sum = curr1.val + curr2.val
            new_node = ListNode(sum) 
            if sum >= 10:
                mp[new_node] += 1
            if prev:
                prev.next = new_node
                new_node.val += mp[prev]
            curr1, curr2 = curr1.next, curr2.next
            prev = new_node"""