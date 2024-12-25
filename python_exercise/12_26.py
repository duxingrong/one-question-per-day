"""
岛屿的周长

给定一个row*col的二维网络地图grid,其中:grid[i][j]=1表示陆地,grid[i][j]=0表示水域

网络中的格子水平和垂直方向相连(对角线方向不连接).整个网络被水完全包围,但其中恰好有一个岛屿
(或者说,一个或多个表示陆地的格子相连组成的岛屿).

岛屿中没有"湖"("湖"指水域在岛屿内部且不和岛屿周围的水相连接)

"""
from typing import List

class Solution():
    def islandPerimeter(self,grid:List[List[int]])->int:
        
        def dfs(grid,x,y,visited,dir):
            visited[x][y] = True
            res = 0
            for i in range(4):
                next_x = dir[i][0]+x
                next_y = dir[i][1]+y
                if next_x<0 or next_x>len(grid)-1 or next_y<0 or next_y>len(grid[0])-1:
                    res+=1  #说明地图外这个方向是水域,周长加1
                elif grid[next_x][next_y]==0:
                    res+=1 #是水域,周长+1
                elif grid[next_x][next_y]==1 and visited[next_x][next_y]==False:
                    res+=dfs(grid,next_x,next_y,visited,dir) #是陆地,深搜
            return res  
        
        #深搜方向
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        result = 0  #记录边长总数
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]


        #首先遍历地图,找到一个陆地
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1 : #说明找到了陆地,开始深搜
                    result = dfs(grid,i,j,visited,dir)
                    return result


if __name__=="__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    solution = Solution()
    print(solution.function(grid))