class Solution:
    def isValidSudoku(self, board):
        # initiate place holder dictionaries
        rows ={}
        cols ={}
        subGrids ={}
        
        # create place holder arrays for  each row,col and subgrids
        #  here is subgrid layout
        # [0][1][2]
        # [3][4][5]
        # [6][7][8]
        for i in range(9):
            rows[i]= []
            cols[i] = []
            subGrids[i]= []
        
        for r in range(9):
            sg_row_id = 0
            if r> 2: sg_row_id = 3
            if r> 5: sg_row_id = 6
            for c in range(9):
                if board[r][c] in rows[r]: return False
                if board[r][c] in cols[c]: return False
                if board[r][c] in subGrids[sg_row_id + (c//3)]: return False
                if board[r][c]!= ".":
                    rows[r].append(board[r][c])
                    cols[c].append(board[r][c])
                    subGrids[sg_row_id + (c//3)].append(board[r][c])
        
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

obj = Solution()
print(obj.isValidSudoku(board))