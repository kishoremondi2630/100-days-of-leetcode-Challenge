class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        if n == 1:
            return 1
        
        # Hardcoded directions for maximum speed
        dirs = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        
        # Two arrays for BFS levels (reduces memory allocation)
        current_level = [(0, 0)]
        grid[0][0] = 1
        distance = 1
        
        while current_level:
            distance += 1
            next_level = []
            
            for row, col in current_level:
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        if r == n-1 and c == n-1:
                            return distance
                        
                        grid[r][c] = 1
                        next_level.append((r, c))
            
            current_level = next_level
        
        return -1
