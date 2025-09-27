# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return "None,"
            return str(node.val) + "," + preorder(node.left) + preorder(node.right)
        
        return preorder(root)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            val = next(nodes)
            if val == "None":
                return None
            
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node
        
        nodes_iter = iter(data.split(","))
        return build_tree(nodes_iter)
