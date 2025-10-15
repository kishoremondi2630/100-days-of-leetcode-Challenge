class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        # Directions for moving to adjacent cells
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def bfs(starts):
            """Perform BFS from starting positions and return reachable cells"""
            queue = collections.deque(starts)
            visited = set(starts)
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # Check boundaries and if we can flow from new cell to current cell
                    if (0 <= nx < m and 0 <= ny < n and 
                        (nx, ny) not in visited and 
                        heights[nx][ny] >= heights[x][y]):
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return visited
        
        # Pacific Ocean starts (top and left edges)
        pacific_starts = []
        for i in range(m):
            pacific_starts.append((i, 0))  # left edge
        for j in range(n):
            pacific_starts.append((0, j))  # top edge
        
        # Atlantic Ocean starts (bottom and right edges)
        atlantic_starts = []
        for i in range(m):
            atlantic_starts.append((i, n-1))  # right edge
        for j in range(n):
            atlantic_starts.append((m-1, j))  # bottom edge
        
        # Find cells that can reach each ocean
        pacific_reachable = bfs(pacific_starts)
        atlantic_reachable = bfs(atlantic_starts)
        
        # Find intersection
        result = pacific_reachable & atlantic_reachable
        
        return [[r, c] for r, c in result]
