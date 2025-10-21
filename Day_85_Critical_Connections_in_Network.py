class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize arrays for discovery time and low value
        disc = [-1] * n  # Discovery time of each node
        low = [-1] * n   # Lowest discovery time reachable from the node
        parent = [-1] * n # Parent of each node in DFS tree
        
        time = [0]  # Use list to pass by reference
        result = []
        
        def dfs(u):
            # Initialize discovery time and low value
            disc[u] = time[0]
            low[u] = time[0]
            time[0] += 1
            
            for v in graph[u]:
                # If v is not visited
                if disc[v] == -1:
                    parent[v] = u
                    dfs(v)
                    
                    # Check if the subtree rooted at v has a connection to ancestors of u
                    low[u] = min(low[u], low[v])
                    
                    # If the lowest vertex reachable from subtree under v is below u,
                    # then u-v is a bridge
                    if low[v] > disc[u]:
                        result.append([u, v])
                
                # If v is visited and not parent of u, update low value
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
        
        # Run DFS for all unvisited nodes
        for i in range(n):
            if disc[i] == -1:
                dfs(i)
        
        return result
