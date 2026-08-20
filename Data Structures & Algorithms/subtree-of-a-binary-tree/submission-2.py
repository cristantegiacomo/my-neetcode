# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        q = deque([root])

        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False



    def isSameTree(self, root, subRoot):
        q = deque([(root, subRoot)])

        while q:
            node, sub = q.popleft()
            if not node and not sub:
                continue
            if not node or not sub:
                return False

            if node.val != sub.val:
                return False
            else:
                q.append((node.left, sub.left))
                q.append((node.right, sub.right))
        return True