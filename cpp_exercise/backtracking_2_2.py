from typing import List

class Solution:
    """
    用于解决N皇后问题的类。
    N皇后问题要求在N×N的棋盘上放置N个皇后，使得它们彼此不能相互攻击。
    """

    def __init__(self):
        """
        初始化Solution类的实例。
        创建用于记录结果和跟踪列、对角线和反对角线占用情况的数据结构。
        """
        self.result = []
        self.cols = set()
        self.diagonals = set()
        self.back_diagonals = set()
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        解决N皇后问题。
        
        Args:
            n: 棋盘的大小和皇后的数量。
            
        Returns:
            List[List[str]]: 所有可能的N皇后解决方案，每个解决方案表示为字符串列表，
            其中'Q'表示皇后的位置，'.'表示空位置。
        """
        self.result.clear()
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.backtracking(0, n, board)
        return self.result
        
    def backtracking(self, row: int, n: int, board: List[List[str]]):
        """
        使用回溯算法解决N皇后问题。
        
        Args:
            row: 当前处理的行。
            n: 棋盘的大小。
            board: 当前棋盘状态。
            
        Returns:
            None: 结果将添加到self.result中。
        """
        # 终止条件
        if row == n:
            self.result.append(["".join(row) for row in board])
            return 
        # 遍历
        for col in range(n):
            diagonal = row - col
            backdiagonal = row + col
            if col in self.cols or diagonal in self.diagonals or backdiagonal in self.back_diagonals:
                continue
            board[row][col] = 'Q'
            self.cols.add(col)
            self.diagonals.add(diagonal)
            self.back_diagonals.add(backdiagonal)
            self.backtracking(row+1, n, board)
            # 回溯
            board[row][col] = '.'
            self.cols.remove(col)
            self.diagonals.remove(diagonal)
            self.back_diagonals.remove(backdiagonal)

if __name__ == "__main__":
    solution = Solution()
    result = solution.solveNQueens(4)
    print(result)
