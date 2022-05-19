# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        maxdepth = -float('inf')
        
        if not root:
            return 0
        
        temp_stack = [(1,root)]
        
        while temp_stack:
            depth, current_node = temp_stack.pop()
            
            if not current_node.left and not current_node.right:
                maxdepth = max(depth, maxdepth)
            
            if current_node.right:
                
                temp_stack.append((depth+1, current_node.right))
                
            
            if current_node.left:
                temp_stack.append((depth+1, current_node.left))
                
        return maxdepth
        