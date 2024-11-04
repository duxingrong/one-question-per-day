"""
给定一个由1陆地和0水组成的矩阵，岛屿指的是由水平或者垂直方向上相邻的陆地单元格组成的区域，且完全被水域单元格包围,孤岛是那些位于矩阵内部，所有的单元格都不接触边缘的岛屿

现在你需要计算所有孤岛的总面积，岛屿面积的计算方式为组成岛屿的陆地的总数

输入描述:
第一行包含两个整数N，M，表示矩阵的行数和列数，之后N行，每行包含M个数字，数字为1或者0

输出描述:
输出一个整数，表示所有孤岛的总面积，如果不存在孤岛，则输出0

本题要求找到不靠边的陆地面积，那么我们只要从周边找到陆地然后 通过 dfs或者bfs 将周边靠陆地且相邻的陆地都变成海洋，然后再去重新遍历地图 统计此时还剩下的陆地就可以了。
"""

class Solution():
    def __init__(self):
        self.graph=[]
        self.dir=[[0,1],[1,0],[-1,0],[0,-1]]
        self.result = 0

    def main(self):
        n,m = map(int,input().split())

        for _ in range(n):
            self.graph.append(list(map(int,input().split())))


        for i in range(m):
            if self.graph[0][i]==1 :
                self.graph[0][i]=0
                self.dfs(0,i)
            if self.graph[n-1][i]==1:
                self.graph[n-1][i]=0
                self.dfs(n-1,i)

        for i in range(1,n-1):
            if self.graph[i][0]==1:
                self.graph[i][0]=0
                self.dfs(i,0)
            if self.graph[i][m-1]==1:
                self.graph[i][m-1]=0
                self.dfs(i,m-1)
        
        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==1:
                    self.result+=1
        print(self.result)

    def dfs(self,x,y):
        for i in range(4):
            next_x = x+self.dir[i][0]
            next_y = y+self.dir[i][1]
            if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]==1 :
                self.graph[next_x][next_y]=0
                self.dfs(next_x,next_y)
                
solution = Solution()
solution.main()
