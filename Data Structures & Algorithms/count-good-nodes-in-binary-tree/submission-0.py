# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)

    
    def dfs(self, node, val_padre):
        if not node:
            return 0

        max_val = max(node.val, val_padre)
        if max_val == node.val:  # node.val >= val_padre
            add = 1
        else:
            add = 0

        return (add + self.dfs(node.left, max_val) 
                + self.dfs(node.right, max_val))





        
