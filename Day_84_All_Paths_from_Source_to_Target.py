class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, path):
            # If we reached the target node
            if node == len(graph) - 1:
                result.append(path[:])  # Add a copy of current path
                return
            
            # Explore all neighbors
            for neighbor in graph[node]:
                path.append(neighbor)  # Choose
                dfs(neighbor, path)    # Explore
                path.pop()             # Unchoose (backtrack)
        
        result = []
        dfs(0, [0])  # Start from node 0 with path [0]
        return result
