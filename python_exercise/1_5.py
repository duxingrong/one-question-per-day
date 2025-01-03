"""
解数独

编写一个程序，通过填充空格来解决数独问题

数独的解法需要遵循如下的规则:
1. 数字1-9在每一行只能出现一次
2. 数字1-9在每一列只能出现一次
3. 数字1-9在每一个以粗实现分隔的3*3宫内只能出现一次

可以使用 最小剩余值（MRV） 策略来选择待填充的空格，即优先填充限制最多的空格。这通常能大大减少递归次数。
"""
from typing import List


class Solution:

    ## 主程式
    def solveSudoku(self,board:List[List[str]])->None:
        self.board = board
        self.dfs()


    def dfs(self)->bool:

        min_choices = float('inf')
        best_pos = None

        ## 遍历board,去找为"."的位置
        for row in range(9):
            for col in range(9):
                if self.board[row][col]=='.':
                    ## 统计此位置的可选数字数量
                    choices = self.get_choices(row,col)
                    if len(choices)<min_choices:
                        min_choices = len(choices)
                        best_pos = (row,col)


            
        ## 如果没有，说明找完了
        if not best_pos:
            return True

        row, col = best_pos

        ## 尝试所有数字
        for num in map(str,range(1,10)):
            if num in self.get_choices(row,col): ## 如果这个数字可以填入这个位置,就进入深搜了
                self.board[row][col]=num
                if self.dfs():
                    return True
                else:
                    self.board[row][col]='.'
        return False
    

    def get_choices(self,row,col):
        choices = set(map(str,range(1,10)))
        ## 如何用一层for循环遍历位置所有位置呢?压缩映射,我们可以通过row,col知道他所在的是第几个3*3的rect,然后通过positon//3确定在第几行,position%3确定在第几列
        for i in range(9):
            rectrow = 3*(row//3)+ i//3
            rectcol = 3*(col//3)+ i%3
            
            choices.discard(self.board[row][i])
            choices.discard(self.board[i][col])
            choices.discard(self.board[rectrow][rectcol])
        return choices


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
