"""
N皇后||
n皇后问题研究的是如何将n个皇后放置在n*n的棋盘上,并且使皇后彼此之间不能相互攻击

同一行，同一列，同一对角线都会攻击

"""

class Solution():
    def __init__(self):
        self.result = 0 #用来记录次数
        self.cols = set() #列去重
        self.diags1 = set()#正对角线
        self.diags2 = set()#副对角线

    #用来深搜答案 
    def dfs(self,n,row):
        if row == n: #说明到底了
            self.result +=1 
            return 

        #遍历每一列
        for col in range(n):
            diag1 = col - row
            diag2 = col + row
            #开始筛选
            if col in self.cols or diag1 in self.diags1 or diag2 in self.diags2:
                continue

            #去重
            self.cols.add(col)
            self.diags1.add(diag1)
            self.diags2.add(diag2)

            #递归去下一层
            self.dfs(n,row+1)

            #回溯
            self.cols.remove(col)
            self.diags1.remove(diag1)
            self.diags2.remove(diag2)

    def totalNQueens(self,n):
        self.dfs(n,0)
        return self.result

            

