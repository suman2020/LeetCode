# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        # levels: 3
        # no of nodes in perfect binary tree: 2^levels -1
        """
        # https://www.youtube.com/watch?v=CvrPf1-flAA
        
        # https://www.youtube.com/watch?v=JxIf7Rs9nPw ....this one
        
        if not root: return 0
        
        def lheight(node):
            if not node: return 0
            return 1+lheight(node.left)
        
        def rheight(node):
            if not node: return 0
            return 1+rheight(node.right)
        
        l,r = lheight(root), rheight(root)
        
        # is this balanced
        if l==r:
            return(2**l)- 1
        
        # if not balanced 
        
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
        
        
        