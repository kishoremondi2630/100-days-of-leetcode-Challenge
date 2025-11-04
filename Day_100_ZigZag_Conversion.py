class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create rows
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            # Add character to current row
            rows[current_row] += char
            
            # Change direction if we're at top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to next row
            current_row += 1 if going_down else -1
        
        # Combine all rows
        return ''.join(rows)
