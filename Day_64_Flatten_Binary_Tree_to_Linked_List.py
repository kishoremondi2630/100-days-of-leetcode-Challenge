# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None   # Keeps track of previously visited node
        
        def dfs(node):
            if not node:
                return
            
            # Traverse in reverse preorder: Right -> Left -> Node
            dfs(node.right)
            dfs(node.left)
            
            # Rewire connections
            node.right = self.prev
            node.left = None
            self.prev = node  # Move prev pointer to current
        
        dfs(root)
        
