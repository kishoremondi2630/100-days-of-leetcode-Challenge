# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_index_map = {}
        for i, val in enumerate(inorder):
            inorder_index_map[val] = i
        
        def build(pre_start, pre_end, in_start, in_end):
            # Base case: no elements to process
            if pre_start > pre_end or in_start > in_end:
                return None
            
            # Root is the first element in current preorder segment
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root's position in inorder
            root_index = inorder_index_map[root_val]
            
            # Calculate sizes of left and right subtrees
            left_size = root_index - in_start
            
            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size, 
                            in_start, root_index - 1)
            root.right = build(pre_start + left_size + 1, pre_end,
                             root_index + 1, in_end)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
