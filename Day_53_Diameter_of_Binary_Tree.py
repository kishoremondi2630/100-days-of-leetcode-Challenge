# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        stack = []
        depth = {}
        diameter = 0
        stack.append(root)
        depth[None] = 0
        
        while stack:
            node = stack[-1]
            if node.left in depth and node.right in depth:
                stack.pop()
                left_depth = depth[node.left]
                right_depth = depth[node.right]
                depth[node] = 1 + max(left_depth, right_depth)
                diameter = max(diameter, left_depth + right_depth)
            else:
                if node.left and node.left not in depth:
                    stack.append(node.left)
                elif node.right and node.right not in depth:
                    stack.append(node.right)
        
        return diameter
