class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        # Maps subtree representation to unique ID
        subtree_to_id = {}
        # Count occurrences of each ID
        count = {}
        # Store result nodes
        result = []
        # ID counter
        id_counter = [1]  # Use list to make it mutable
        
        def traverse(node):
            if not node:
                return 0
            
            # Get IDs for left and right subtrees
            left_id = traverse(node.left)
            right_id = traverse(node.right)
            
            # Create unique representation
            repr_key = (node.val, left_id, right_id)
            
            # Get or create ID for this representation
            if repr_key in subtree_to_id:
                subtree_id = subtree_to_id[repr_key]
            else:
                subtree_id = id_counter[0]
                subtree_to_id[repr_key] = subtree_id
                id_counter[0] += 1
            
            # Update count
            count[subtree_id] = count.get(subtree_id, 0) + 1
            
            # Add to result if this is the second occurrence
            if count[subtree_id] == 2:
                result.append(node)
            
            return subtree_id
        
        traverse(root)
        return result
