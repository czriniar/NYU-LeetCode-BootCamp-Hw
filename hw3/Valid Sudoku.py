class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid_row(row):
            seen = set()
            for num in row:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        def is_valid_column(col):
            seen = set()
            for num in col:
                if num != '.':
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        def is_valid_box(start_row, start_col):
            seen = set()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    num = board[i][j]
                    if num != '.':
                        if num in seen:
                            return False
                        seen.add(num)
            return True

        # Check rows
        for i in range(9):
            if not is_valid_row(board[i]):
                return False

        # Check columns
        for j in range(9):
            if not is_valid_column([board[i][j] for i in range(9)]):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_box(i, j):
                    return False

        return True
