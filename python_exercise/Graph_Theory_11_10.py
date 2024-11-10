"""
给定一个由1陆地和0水组成的矩阵，岛屿是被水包围，并且通过水平方向或者垂直方向上相邻的陆地连接而成的
你可以假设矩阵外均被水包围，在矩阵中恰好拥有一个岛屿，假设组成岛屿的陆地边长都为1，请计算岛屿的周长。岛屿的内部没有水域

输入描述:
第一行包含两个整数N，M，表示矩阵的行数和列数。之后N行，每行包含M个数字，数字1或者0,表示岛屿的单元格

输出描述:
输出一个整数，表示岛屿的周长
"""

class Solution():
    def __init__(self):
        self.graph = []
        self.result= 0
        self.dir = [[0,1],[1,0],[0,-1],[-1,0]]

    def main(self):
        n,m = map(int,input().split())
        for _ in range(n):
            self.graph.append(list(map(int,input().split())))

        self.visited = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==1 and not self.visited[i][j]:
                    self.visited[i][j]=True
                    self.result= self.dfs(i,j)

        print(self.result)


    def dfs(self,x,y):
        count = 4  #一共四条边，只要有一条边连接了陆地，那就-1
        for i in range(4):
            next_x = x+self.dir[i][0]
            next_y = y+self.dir[i][1]       
            if next_x< 0 or next_x>=len(self.graph) or next_y<0 or next_y>=len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]==1 :
                count-=1
                if not self.visited[next_x][next_y]:
                    self.visited[next_x][next_y]=True
                    count+=self.dfs(next_x,next_y)
        return count


    
solution =Solution()
solution.main()
