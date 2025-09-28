# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')
        self._dfs(root)
        return self.max_sum
    
    def _dfs(self, node):
        if not node:
            return 0
        
        # Get max path sums from left and right (ignore negative sums)
        left = max(0, self._dfs(node.left))
        right = max(0, self._dfs(node.right))
        
        # Update global maximum with path through current node
        self.max_sum = max(self.max_sum, node.val + left + right)
        
        # Return max single path sum
        return node.val + max(left, right)
