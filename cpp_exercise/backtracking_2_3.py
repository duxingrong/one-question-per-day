from typing import List

class Solution:
    """
    解数独，也就是填满9*9的格子，保证row ,col,以及3*3的小格子中没有重复数字
    """
    def solveSudoku(self,board:List[List[str]])->None:
        """
        主函数
        Args: 
            board: 九x九的棋盘
        Returns:
            None: 直接在原board上修改
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num!='.':
                    row_used[row].add(num)
                    col_used[col].add(num)
                    box_used[3*(row//3)+col//3].add(num)
        self.backtracking(0,0,row_used,col_used,box_used,board)


    def backtracking(self,
                     row:int,
                     col:int,
                     row_used:List[List[str]],
                     col_used:List[List[str]],
                     box_used:List[List[str]],
                     board:List[List[str]]
                     )->bool:
        if row == 9:
            return True
        next_row,next_col = (row,col+1) if col<8 else (row+1,0)
        if board[row][col]!=".":
            return self.backtracking(next_row,next_col,row_used,col_used,box_used,board)
        else:
            for num in map(str,range(1,10)):
                if num in row_used[row] or num in col_used[col] or num in box_used[(row//3)*3+col//3]:
                    continue
                board[row][col]=num
                row_used[row].add(num)
                col_used[col].add(num)
                box_used[(row//3)*3+col//3].add(num)
                if self.backtracking(next_row,next_col,row_used,col_used,box_used,board):
                    return True
                board[row][col]='.'
                row_used[row].remove(num)
                col_used[col].remove(num)
                box_used[(row//3)*3+col//3].remove(num)
            return False





if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solver = Solution()
    solver.solveSudoku(board)

    # 输出解数独的结果
    for row in board:
        print(row)















