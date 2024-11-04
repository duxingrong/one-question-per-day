"""
给定一个由1(陆地)和0(水)组成的矩阵，计算岛屿的最大面积，岛屿面积的计算方式为组成岛屿的陆地的总数，岛屿由水平方向或垂直方向上相邻的陆地连续而成，并且四周都是水域，你可以假设矩阵外均被水包围

第一行包含两个整数N,M,表示矩阵的行数和列数，后续N行，每行包含M个数字，数字为1或者0,表示岛屿的单元格

输出一个整数，表示岛屿的最大面积，如果不存在岛屿，则输出0.
"""


"""
深搜
"""
class Solution():
    def __init__(self):
        self.dir=[[0,1],[1,0],[0,-1],[-1,0]]
        self.graph=[]
        self.ans=0  

    def main(self):
        #接收矩阵
        n,m = map(int,input().split())
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))

        self.visited= [[False]*m for _ in range(n)]

        #寻找最大岛屿
        for i in range(n):
            for j in range(m):
                #如果发现岛屿并且标志位为False
                if self.graph[i][j]==1 and self.visited[i][j]==False:
                    ans=1 #发现了一块陆地
                    self.visited[i][j]=True
                    ans+=self.dfs(i,j)
                    self.ans=max(ans,self.ans)
        print(self.ans)

    def dfs(self,x,y):
        area=0 
        #探索四个方向
        for i in range(4):
            next_x=x+self.dir[i][0]
            next_y=y+self.dir[i][1]
            if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]==1 and not self.visited[next_x][next_y]:
                area+=1
                self.visited[next_x][next_y]=True
                area+=self.dfs(next_x,next_y)
        return area




"""
广搜
"""
from collections import deque

class Solution():
    def __init__(self):
        self.dir=[[0,1],[1,0],[0,-1],[-1,0]]
        self.graph=[]
        self.ans=0  

    def main(self):
        #接收矩阵
        n,m = map(int,input().split())
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))

        self.visited= [[False]*m for _ in range(n)]

        #寻找最大岛屿
        for i in range(n):
            for j in range(m):
                #如果发现岛屿并且标志位为False
                if self.graph[i][j]==1 and self.visited[i][j]==False:
                    ans=1 #发现了一块陆地
                    self.visited[i][j]=True
                    ans+=self.bfs(i,j)
                    self.ans=max(ans,self.ans)
        print(self.ans)

    def bfs(self,x,y):
        area=0
        q = deque([])
        q.append([x,y])
        while  q:
            cur_x,cur_y=q.popleft()
            for i in range(4):
                next_x = cur_x+self.dir[i][0]
                next_y = cur_y+self.dir[i][1]
                if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                    continue
                if self.graph[next_x][next_y]==1 and  not self.visited[next_x][next_y]:
                    self.visited[next_x][next_y]=True
                    area+=1
                    q.append([next_x,next_y])
        return area



solution=Solution()
solution.main()


        
