# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if abs(self.height(root.left)-self.height(root.right)) <= 1:
            res_left = self.isBalanced(root.left)    #false
            res_right = self.isBalanced(root.right)   #true
        else:
            return False
        
        return res_left and res_right
        


    def height(self, node):
        if not node:
            return 0
        
        return 1+ max(self.height(node.left,),
                     self.height(node.right))