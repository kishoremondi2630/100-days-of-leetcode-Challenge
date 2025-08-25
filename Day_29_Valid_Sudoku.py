class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check each row
        for i in range(9):
            seen = set()
            for j in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        
        # Check each column
        for j in range(9):
            seen = set()
            for i in range(9):
                cell = board[i][j]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        
        # Check each 3x3 sub-box
        for box in range(9):
            # Calculate the top-left corner of each sub-box
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3
            seen = set()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    cell = board[i][j]
                    if cell != '.':
                        if cell in seen:
                            return False
                        seen.add(cell)
        
        return True
