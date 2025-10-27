class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Initialize bitmasks
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        # Fill initial constraints
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    mask = 1 << (num - 1)
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i//3)*3 + (j//3)] |= mask
                else:
                    empty_cells.append((i, j))
        
        self.solve_bitmask(board, rows, cols, boxes, empty_cells)
    
    def solve_bitmask(self, board, rows, cols, boxes, empty_cells):
        if not empty_cells:
            return True
        
        # Find cell with fewest possibilities
        min_idx = 0
        min_options = 10
        for idx, (i, j) in enumerate(empty_cells):
            box_idx = (i//3)*3 + (j//3)
            used = rows[i] | cols[j] | boxes[box_idx]
            options = 9 - bin(used).count('1')
            if options < min_options:
                min_options = options
                min_idx = idx
                if min_options == 1:  # Early exit if only one option
                    break
        
        i, j = empty_cells[min_idx]
        empty_cells[min_idx], empty_cells[-1] = empty_cells[-1], empty_cells[min_idx]
        empty_cells.pop()
        
        box_idx = (i//3)*3 + (j//3)
        used = rows[i] | cols[j] | boxes[box_idx]
        
        for num in range(1, 10):
            mask = 1 << (num - 1)
            if not (used & mask):
                # Place number
                board[i][j] = str(num)
                rows[i] |= mask
                cols[j] |= mask
                boxes[box_idx] |= mask
                
                if self.solve_bitmask(board, rows, cols, boxes, empty_cells):
                    return True
                
                # Backtrack
                board[i][j] = '.'
                rows[i] &= ~mask
                cols[j] &= ~mask
                boxes[box_idx] &= ~mask
        
        empty_cells.append((i, j))
        return False
