"""
现有一个NxM的矩阵，每个单元格包含一个数值，这个数值代表该位置的相对高度，矩阵的左边界和上边界被认为是第一组边界，而矩阵的右边界和下边界被视为第二组边界

矩阵模拟了一个地形，当雨水落在上面时，水会根据地形的倾向向底处流动，但只能从较高或等高的地点流向较低或者等高并且相邻(上下左右方向)的地点.我们的目标是确定那些单元格，从这些单元格出发的水可以达到第一组边界和第二组边界

输出描述:
第一行包含两个整数N和M，分别表示矩阵的行数和列数
后序N行，每行包含M个整数，表示矩阵的每个单元格的高度

输出描述:
输出共有多行，每行输出两个整数，用一个空格隔开，表示可到达第一组边界和第二组边界的单元格的坐标，输出顺序任意
"""

class Solution():
    def __init__(self):
        self.graph = []
        self.dir = [[0,1],[1,0],[-1,0],[0,-1]]

    def main(self):
        n,m = map(int,input().split())
        #填充地图
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))
        #设置标签
        self.oneTag = [[False]*m for _ in range(n)]
        self.twoTag = [[False]*m for _ in range(n)]       

        #开始遍历
        #第一边界标记
        for j in range(m):
            self.oneTag[0][j]=True
            self.dfs(0,j,self.oneTag)
        for i in range(1,n):
            self.oneTag[i][0]=True
            self.dfs(i,0,self.oneTag)

        #第二边界标记
        for j in range(m):
            self.twoTag[n-1][j]=True
            self.dfs(n-1,j,self.twoTag)
        for i in range(1,n):
            self.twoTag[i][m-1]=True
            self.dfs(i,n-1,self.twoTag)

        #遍历满足条件的结果
        for i in range(n):
            for j in range(m):
                if self.oneTag[i][j] and self.twoTag[i][j]:
                    result = str(i) + " " + str(j)
                    print(result)

    def dfs(self,x,y,Tag):
        for i in range(4):
            next_x = x+self.dir[i][0]
            next_y = y+self.dir[i][1]
            if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]>=self.graph[x][y] and not Tag[next_x][next_y]:
                Tag[next_x][next_y]=True
                self.dfs(next_x,next_y,Tag)


solution = Solution()
solution.main()

