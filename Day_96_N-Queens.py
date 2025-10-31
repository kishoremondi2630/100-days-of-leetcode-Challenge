class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return [[""]]
        if n == 1:
            return [["Q"]]
        
        solutions = []
        stack = [(0, 0, 0, 0, [])]  # (row, cols, diag1, diag2, queens)
        
        while stack:
            row, cols, diag1, diag2, queens = stack.pop()
            
            if row == n:
                # Build solution
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - col - 1))
                solutions.append(board)
                continue
            
            # Get available positions
            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
            
            while available:
                col_bit = available & -available
                available &= available - 1
                col_index = col_bit.bit_length() - 1
                
                # Push new state to stack
                stack.append((
                    row + 1,
                    cols | col_bit,
                    (diag1 | col_bit) << 1,
                    (diag2 | col_bit) >> 1,
                    queens + [col_index]
                ))
        
        return solutions
