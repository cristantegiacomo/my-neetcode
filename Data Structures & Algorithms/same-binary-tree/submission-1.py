# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queueP = deque()
        queueQ = deque()
        dummy = TreeNode(101)   #se metti come default 0 su leetcode non passa perché puoi avere p=[1,0] e q=[1,null,0] e nel mio codice passerebbero enrambi

        if p: queueP.append(p)
        if q: queueQ.append(q)

        while queueP and queueQ:
            P_node = queueP.popleft()
            Q_node = queueQ.popleft()

            if P_node.val != Q_node.val:
                return False

            if P_node.left: queueP.append(P_node.left)
            elif P_node!=dummy: queueP.append(dummy)
            if P_node.right: queueP.append(P_node.right)
            elif P_node!=dummy: queueP.append(dummy)

            if Q_node.left: queueQ.append(Q_node.left)
            elif Q_node!=dummy: queueQ.append(dummy)
            if Q_node.right: queueQ.append(Q_node.right)
            elif Q_node!=dummy: queueQ.append(dummy)
        
        if queueP or queueQ:
            return False
        
        return True