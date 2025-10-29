class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)  # Add extra element for easier calculation
        max_area = 0
        
        for i in range(rows):
            # Update heights for current row
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Calculate largest rectangle in current histogram
            stack = []
            for j in range(cols + 1):
                while stack and heights[j] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(j)
        
        return max_area
