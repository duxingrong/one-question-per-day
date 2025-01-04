"""
N皇后

按照国际象棋的规则,皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子.

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上,并且使皇后彼此之间不能相互攻击.

给你一个整数 n ,返回所有不同的 n 皇后问题 的解决方案.

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案,该方案中 'Q' 和 '.' 分别代表了皇后和空位.
"""

from typing import List


class Solution:
    def __init__(self):
        ## 用集合记录
        self.cols = set()
        self.diag1 = set()
        self.diag2 = set()
        self.result = []


    def solveNQueens(self,n:int)->List[List[str]]:

        ## board
        self.board = [ ["."]*n for _ in range(n)]
        self.dfs(0,n)
        return self.result

        
    def dfs(self,row,n):
        ## 终止的时候也是收获结果的时候
        if row == n:
            self.result.append(["".join(row) for row in self.board])
            return 

        for col in range(n):
            diag1 = row-col
            diag2 = row+col
            if col in self.cols or diag1 in self.diag1 or diag2 in self.diag2:
                continue

            # 如果这个位置可以
            self.board[row][col] = "Q"
            self.cols.add(col)
            self.diag1.add(diag1)
            self.diag2.add(diag2)

            self.dfs(row+1,n)

            ## 回溯
            self.board[row][col] ="."
            self.cols.remove(col)
            self.diag1.remove(diag1)
            self.diag2.remove(diag2)


if __name__ == "__main__":
    solution = Solution()
    results = solution.solveNQueens(4)
    number = 0
    for result in results:
        for row in result:
            print(row)
        number+=1
        print(number)



            
        
        
        

