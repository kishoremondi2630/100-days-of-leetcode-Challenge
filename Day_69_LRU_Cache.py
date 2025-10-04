class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  # key -> node
        
        # Dummy head and tail for the doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        """Remove an existing node from the linked list"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        """Move certain node to the head (most recently used)"""
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        """Pop the current tail (least recently used)"""
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        return tail_node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)  # Mark as recently used
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # Key exists, update value and move to head
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            # New key
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # Check if we exceeded capacity
            if len(self.cache) > self.capacity:
                # Remove the least recently used item
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
