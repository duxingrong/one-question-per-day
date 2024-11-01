"""
给定一个由1(陆地)和0(水)组成的矩阵，你需要计算岛屿的数量,岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域，你可以假设矩阵外均被水包围

输入描述:
第一行包含两个整数N,M,表示矩阵的行数和列数.
后续N行，每行包含M个数字，数字1或者0.

输出描述:
输出一个整数，表示岛屿的数量，如果不存在岛屿，则输出0

4 5 
1 1 0 0 0 
1 1 0 0 0 
0 0 1 0 0 
0 0 0 1 1 

3
"""


class Solution():
    def __init__(self):
        self.dir = [[0,1],[1,0],[0,-1],[-1,0]] #四个方向
        self.graph = [] #地图
        self.result=0 #结果，岛屿的数量

    def main(self):
        #接受n和m
        n,m = map(int,input().split())
        for _ in range(n):
            self.graph.append(list(map(int,input().split()))) #填充地图

        #设置访问表
        self.visited = [[False]*m for _ in range(n)]

        #开始找岛屿
        for i in range(n):
            for j in range(m):
                #如果遍历到陆地，并且它还没有被标记
                if self.graph[i][j]==1 and not self.visited[i][j]:
                    self.result+=1
                    self.visited[i][j]=True
                    self.dfs(self.graph,self.visited,i,j)
        print(self.result)

    def dfs(self,graph,visited,x,y):
        #它的目的就是将陆地旁边的所有陆地全部变成True，防止再次重复记录
        for  i in range(4):
            nextx= x+self.dir[i][0]
            nexty = y+self.dir[i][1]
            #判断是否越界
            if nextx<0 or nextx>=len(graph) or nexty<0 or nexty>=len(graph[0]):
                continue
            if self.graph[nextx][nexty]==1 and  not self.visited[nextx][nexty]:
                self.visited[nextx][nexty]=True
                self.dfs(graph,visited,nextx,nexty)

if __name__=="__main__":        
    solution = Solution()
    solution.main()


