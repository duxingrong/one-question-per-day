"""
一个数独的解法需遵循如下规则,数字1-9在每一行只能出现一次,数字1-9在每一列只能出现一次.数字1-9在每一个以粗实线分隔的3*3宫内只出现一次,空白格"."表示 求出一个解就好
"""


"""
难点:
怎么判断3*3的宫内只出现一次
一行不止选一个,说明不能选了就下一层,而是要遍历所有'.'的位置
如何写终止条件(目前知道是求一个解,那就是有返回值bool)
"""

"""
三步骤:
1.参数:一个二维的棋盘List[List[str]] 返回:一个新的棋盘
2. 终止条件: 当把棋盘所有的'.'的位置都填入数字后,就终止(True),可以理解为遍历结束,或者一个位置,当我们不管上面是怎么填入的,这个位置反正是填不了数字,那就是无解,返回(False)
3. 单层逻辑: 
首先是遍历所有,那么二维数组就需要使用两层for循环,去找所有的'.'的位置;找到位置后,开始遍历数字1-9,if 满足要求(行列九宫格都不重复)就递归去找下一个'.'的空格,如果下一层也能返回True,如果一路都可以,那就遍历完了达到终止条件True ; 如果中途有一个'.'填入失败,那就是回溯,将上一个位置撤回成'.'让它再取另外的数字,然后再尝试,如果当前层所有的数字都无法使得下一层为True,那就是return False,继续回溯当上一层(如果回溯到最开始都没办法满足,那就是终止条件False无解)
4. is_valid(board,row,col,number)函数
条件一: 元素所在的同一行和同一列不能有相同的元素 
for i in range(9)
if board[row][i]==num or board[i][col]==num: return False
条件二: 判断九宫格內有没有相同的数字(压缩映射法)
如果不压缩,我们二维数组又需要用两层for循环来遍历(low)
可以用3*(row//3)来表示遍历位置所在九宫格的左上角的行
可以用3*(col//3)来表示遍历位置所在九宫格的左上角的列
然后3*(row//3)+i//3来唯一映射当前遍历位置的准确位置了
然后3*(row//3)+i%3来唯一映射当前遍历位置的准确位置了  %是取余数
"""


from typing import List
class Solution():
    # 主函数
    def solveSudoku(self,board:List[List[str]]):
        self.board = board
        self.backtracking()

    # 判断是否有效的函数
    def is_valid(self,board,row,col,num):
        for i in range(9):
            if board[row][i]==num or board[i][col]==num:
                return False
            blockrow=3*(row//3)+i//3
            blockcol=3*(col//3)+i%3
            if board[blockrow][blockcol]==num:
                return False
        return True

    # 递归函数
    def backtracking(self)->bool:
        for row in range(9):
            for col in range(9):
                if self.board[row][col]=='.':
                    # map() 函数的作用是将一个函数应用到一个可迭代对象的每个元素上，并返回一个迭代器。
                    #它可以用来对列表、元组或其他可迭代对象中的元素进行批量处理。
                    for num in map(str,range(1,10)):
                        if self.is_valid(self.board,row,col,num):
                            self.board[row][col]=num
                            # 下一层可以,你才可以
                            if self.backtracking():
                                return True
                            # 下一层不行,你就回溯
                            self.board[row][col]='.'
                    # 如果你遍历完了还满足不了下一层,那就再往上回溯,你这层得返回False,如果到第一层还是不行,这个False会成为终止的False
                    return False
        # 这里只有逐层True到最开始才会走到这里()
        return True
                            
                            
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














