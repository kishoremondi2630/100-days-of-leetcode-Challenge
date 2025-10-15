"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        
        # Pre-allocate for maximum possible nodes
        clones = [None] * 101
        clones[node.val] = Node(node.val)
        queue = collections.deque([node])
        
        while queue:
            curr = queue.popleft()
            curr_clone = clones[curr.val]
            
            for nb in curr.neighbors:
                if not clones[nb.val]:
                    clones[nb.val] = Node(nb.val)
                    queue.append(nb)
                curr_clone.neighbors.append(clones[nb.val])
        
        return clones[node.val]
