# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
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
        return isSameTree(p, q)