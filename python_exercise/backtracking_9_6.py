"""
研究如何将n个皇后放置在nxn的棋盘上,并且使得皇后彼此之间不能相互攻击
同一行,同一列,同一个对角线都会攻击
n=1 或者n>=4才有解
"""

"""
这题其实还是可以明白的,我们用递归去不断进入下一行,单层逻辑处理这一行的哪些列可以取
1.针对一行,那么上面选过的列,他不能再选择,上面如果主对角线有,他也不能选,上面副对角线有值,也不选
这里的精髓在于怎么让我们知道哪些选过呢?
针对列:用一个全局变量used = [False]*n 就可以
针对主对角线:由于主对角线的列-行=0 所以一个n*n的所有位置,除了主对角线上的元素这里会等于0一样,其他位置都是不同的数值
针对副对角线:由于副对角线的列+行=同一个值,所以一个n*n的所有位置,除了副对角线上的元素这里会一样,其他位置都是不同的数值
2. 我们返回所有的情况,一个子列表就是一种棋盘的布局 ,这样就需要初始化棋盘,然后对于皇后的位置,放上"Q",其他位置则是"."
"""

"""
三步骤:
1. 参数:n 返回: List[List[int]]
2. 终止条件: 如果行row==n(因为从0开始遍历的) : 就说明已经是空行了,直接记录结果进结果集,然后return
3. 单层逻辑:
for col in range(n): 计算diag1和diag2;if col in cols  or diag1 in diagonals1 or diag2 in diagonals2: (列重复,主副对角线重复) continue
cols.add()
diagonals1.add()
diagonals2.add()
board[row][col]="Q"
递归
board[row][col]='.'
cols.remove(col)
diagonals1.remove(diag1)
diagonals2.remove(diag2)
"""

from typing import List

class Solution():
    def __init__(self):
        self.cols=set()
        self.diagonals1=set()
        self.diagonals2=set()
        self.result = []
        # self.board = []

    def solveQueens(self,n:int)->List[List[str]]:
        if n<4 and n!=1:
            return self.result
        board= [['.' for _ in range(n)] for _ in range(n)]
        self.backtracking(n,0,board)
        return self.result

    def backtracking(self,n,row,board):
        # 终止条件
        if row ==n:
            self.result.append(["".join(row) for row in board]) # 将每一行变成一个字符串
            return 

        # 单层逻辑
        for col in range(n):
            diag1=row-col
            diag2=row+col
            if col in self.cols or diag1 in self.diagonals1 or diag2 in self.diagonals2:
                continue
            
            self.cols.add(col)
            self.diagonals1.add(diag1)
            self.diagonals2.add(diag2)
            board[row][col]='Q'
            # 递归
            self.backtracking(n,row+1,board)
            # 回溯
            self.cols.remove(col)
            self.diagonals1.remove(diag1)
            self.diagonals2.remove(diag2)
            board[row][col]='.'
        

solution = Solution()
results = solution.solveQueens(4)
number = 0
for result in results:
    for row in result:
        print(row)
    number+=1
    print(number)


















