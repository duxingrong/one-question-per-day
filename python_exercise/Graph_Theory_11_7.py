"""
给定一个由1陆地和0水组成的矩阵，你最多可以将矩阵中的一格水变成一块陆地，在执行了此操作后，矩阵中最大的岛屿面积是多少
岛屿面积的计算方式为组成岛屿的陆地的总数，岛屿是被水包围，并且通过水平方向或者垂直方向上相邻的陆地连接而成的，你可以假设矩阵外均被水包围

输入描述:
第一行包含两个整数N，M,表示矩阵的行数和列数，之后N行，每行包含M个数字，数字为1或者0 ，表示岛屿的单元格

输出描述:
输出一个整数，表示最大的岛屿面积


怎么才能知道最大岛屿呢？

"""

class Solution():
    def __init__(self):
        self.dir = [[0,1],[1,0],[-1,0],[0,-1]]
        self.graph= []
        self.table = {0:0}
        self.result = 0
        
    def main(self):
        n,m=map(int,input().split())

        for _ in range(n):
            self.graph.append(list(map(int,input().split())))


        #如果全是陆地，没有0 ，极端
        if all(cell == 1 for row in self.graph for cell in row):
            print(n*m)
            return 

        self.visited = [[False]*m for _ in range(n)]

        count = 2
        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==1 and not self.visited[i][j]:
                    self.visited[i][j]=True
                    self.graph[i][j]=count
                    sum = 1+self.dfs(i,j,count) 
                    self.table[count]=sum
                    count +=1

        #然后开始遍历所有的0位置
        for i in range(n):
            for j in range(m):
                if self.graph[i][j]==0 :
                    result = 1
                    st= set()
                    if n-1>=i-1>=0 and self.graph[i-1][j] not in st :
                        result+=self.table[self.graph[i-1][j]]
                        st.add(self.graph[i-1][j])
                    if n-1>=i+1>=0 and self.graph[i+1][j] not in st :
                        result+=self.table[self.graph[i+1][j]]
                        st.add(self.graph[i+1][j])
                    if m-1>=j-1>=0 and self.graph[i][j-1] not in st :
                        result+=self.table[self.graph[i][j-1]]
                        st.add(self.graph[i][j-1])
                    if m-1>=j+1>=0 and self.graph[i][j+1] not in st :
                        result+=self.table[self.graph[i][j+1]]
                        st.add(self.graph[i][j+1])
                    self.result=max(result,self.result)
        print(self.result)


    def dfs(self,x,y,count):
        area = 0
        for i in range(4):
            next_x = x+self.dir[i][0]
            next_y = y+self.dir[i][1]
            if next_x<0 or next_x>=len(self.graph)or next_y<0 or next_y>= len(self.graph[0]):
                continue
            if self.graph[next_x][next_y]==1 and not self.visited[next_x][next_y]:
                self.visited[next_x][next_y]=True
                self.graph[next_x][next_y]=count
                area += self.dfs(next_x,next_y,count)+1
        return area
                    
    

solution =Solution()
solution.main()
