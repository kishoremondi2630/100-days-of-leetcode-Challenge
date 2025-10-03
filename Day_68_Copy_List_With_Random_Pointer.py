"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        # Step 1: Create new nodes and interweave them
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set random pointers for new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the interwoven lists
        current = head
        new_head = head.next
        copy_current = new_head
        
        while current:
            current.next = current.next.next
            if copy_current.next:
                copy_current.next = copy_current.next.next
            
            current = current.next
            copy_current = copy_current.next
        
        return new_head
