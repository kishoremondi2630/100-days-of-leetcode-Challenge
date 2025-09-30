"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
            
        current = root
        
        while current and current.left:
            # Use current level to connect the next level
            level_start = current.left
            
            while current:
                # Connect left child to right child
                current.left.next = current.right
                
                # Connect right child to next node's left child
                if current.next:
                    current.right.next = current.next.left
                
                # Move horizontally in current level
                current = current.next
            
            # Move to next level
            current = level_start
            
        return root
