"""
给定一个由1路地和0(水)组成的矩阵，你需要计算岛屿的数量，岛屿由水平或垂直方向上相邻的陆地连接而成，并且四周都是水域，你可以假设矩阵外均被水包围

第一行包含两个整数，N,M 表示矩阵的行数和列数
后续N行，包含M个数字，数字为1或者0

输出一个整数，表示岛屿的数量，如果不存在岛屿，则输出0

广搜使用的是对列来模仿栈
"""
from collections import deque

class Solution():
    def __init__(self):
        self.graph=[]
        self.dir = [[0,1],[1,0],[0,-1],[-1,0]]
        self.result=0
    
    def main(self):
        #首先接受两个参数N，M
        n,m = map(int,input().split())
        #填充地图
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))
        #创建访问表
        self.visited = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==1 and self.visited[i][j]==False:
                    self.result+=1
                    self.visited[i][j]=True
                    self.bfs(self.graph,self.visited,i,j)  #满足条件的才放进来
        print(self.result)

    def bfs(self,graph,visited,x,y):
        queue= deque([])
        queue.append([x,y])
        while queue:
            cur_x ,cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x+self.dir[i][0]
                next_y =  cur_y+self.dir[i][1]
                #限制边界
                if next_x<0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                    continue
                if self.graph[next_x][next_y]==1 and self.visited[next_x][next_y]==False:
                    self.visited[next_x][next_y]=True
                    queue.append([next_x,next_y])
                
if __name__=="__main__":
    solution=Solution()
    solution.main()
