# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
# al posto di controllare quando subtree appartiene a tree (true) e poi vedere se va
# avanti e mettere (false), so che il subroot deve essere perforza alla fine di root.

        if not root:
            return False

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot) 
        
        if self.sameTree(root, subRoot):
            return True
        
        return left or right



    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False