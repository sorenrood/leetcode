class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSquares(board: List[List[str]]) -> bool:
            starts = {1: (0, 0), 2: (0, 3), 3: (0, 6), 
                     4: (3, 0), 5: (3, 3), 6: (3, 6),
                     7: (6, 0), 8: (6, 3), 9: (6, 6)}
            for i in range(1, 10):
                temp = []
                column = starts[i][1]
                row = starts[i][0]
                for s in range(column, column + 3):
                    for j in range(row, row + 3):
                        square = board[j][s]
                        if square == '.':
                            continue
                        elif square in temp:
                            return False
                        else:
                            temp.append(square)
            return True
            
        def checkRows(board):
            for row in board:
                temp = []
                for square in row:
                    if square == '.':
                        continue
                    elif square in temp:
                        return False
                    else:
                        temp.append(square)
            return True
                    
        def checkColumns(board):
            for i in range(0, 9):
                temp = []
                for j in range(0, 9):
                    square = board[j][i]
                    if square == '.':
                        continue
                    elif square in temp:
                        return False
                    else:
                        temp.append(square)
            return True
                    
        return checkSquares(board) and checkRows(board) and checkColumns(board)
        