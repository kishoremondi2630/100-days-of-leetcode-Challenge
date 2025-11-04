class Node:
    __slots__ = ['key', 'val', 'freq', 'prev', 'next']
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    __slots__ = ['head', 'tail', 'size']
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def pop(self, node=None):
        if self.size == 0:
            return None
        if node is None:
            node = self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.min_freq = 0
        self.size = 0
        self.nodes = {}
        self.lists = {}

    def get(self, key):
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.cap == 0:
            return
        
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._update(node)
        else:
            if self.size == self.cap:
                lst = self.lists[self.min_freq]
                node_to_remove = lst.pop()
                del self.nodes[node_to_remove.key]
                self.size -= 1
            
            node = Node(key, value)
            self.nodes[key] = node
            if 1 not in self.lists:
                self.lists[1] = DLinkedList()
            self.lists[1].append(node)
            self.min_freq = 1
            self.size += 1

    def _update(self, node):
        freq = node.freq
        lst = self.lists[freq]
        lst.pop(node)
        
        if freq == self.min_freq and lst.size == 0:
            self.min_freq += 1
        
        node.freq = freq + 1
        new_freq = node.freq
        
        if new_freq not in self.lists:
            self.lists[new_freq] = DLinkedList()
        self.lists[new_freq].append(node)
