"""
给定一个由1陆地和0水组成的矩阵，岛屿指的是由水平或者垂直方向上相邻的陆地单元格组成的区域，且完全被水域单元格包围，孤岛是那些位于矩阵内部，所有单元格都不接触边缘的岛屿

现在你需要将所有孤岛沉没，即将孤岛中的所有陆地单元格1转变成水域单元格0

输入描述:
第一行包含两个整数N,M,表示矩阵的行数和列数
之后N行，每行包含M个数字，数字1或者0,表示孤岛的单元格

输出描述:
输出将孤岛沉没后的岛屿矩阵
"""
	
class Solution():
    def __init__(self):
        self.dir=[[1,0],[0,1],[-1,0],[0,-1]]
        self.graph=[]
     
    def main(self):
        n,m=map(int,input().split())
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))
        self.visited=[[False]*m for _ in range(n)]
         
        for j in range(m):
            if self.graph[0][j]==1 and self.visited[0][j]==False:
                self.visited[0][j]=True
                self.dfs(0,j)
            if self.graph[n-1][j]==1 and self.visited[n-1][j]==False:
                self.visited[n-1][j]=True
                self.dfs(n-1,j)
         
        for i in range(1,n-1):
            if self.graph[i][0]==1 and self.visited[i][0]==False:
                self.visited[i][0]=True
                self.dfs(i,0)
            if self.graph[i][m-1]==1 and self.visited[i][m-1]==False:
                self.visited[i][m-1]=True
                self.dfs(i,m-1)
         
        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==1 and self.visited[i][j]==False:
                    self.graph[i][j]=0
        for ans in self.graph :
            print(" ".join(map(str,ans)))
                 
                 
    def dfs(self,x,y):
        for i in range(4):
            next_x=self.dir[i][0]+x
            next_y=self.dir[i][1]+y
            if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]==1 and self.visited[next_x][next_y]==False:
                self.visited[next_x][next_y]=True
                self.dfs(next_x,next_y)
                 
                 
                 
solution=Solution()
solution.main()
