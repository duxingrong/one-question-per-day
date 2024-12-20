"""
钥匙和房间

有N个房间,开始时你位于0号房间.每个房间有不同的号码:0,1,2,...,N-1,且房间里可能有一些钥匙能使你进入下一个房间.
在形式上,对于每个房间i都有一个钥匙列表rooms[i],每个钥匙rooms[i][j]由[0,1,...,N-1]中的一个整数表示,
其中N=rooms.length。钥匙rooms[i][j]=v可以打开编号为v的房间

最初,除0号房间外的其余所有房间都被锁住
你可以自由地在房间之间来回走动,如果能进入每个房间返回true,否则返回false.

举例: [[1],[2],[3],[]]
输出 true 我们可以进入每个房间

"""

# 这是一个有向图搜索全路径的问题,只能使用dfs和bfs
# 方法都是使用visited来确定哪些房间遍历过,防止死循环

"""
使用dfs的时候,我们需要知道,在当层递归中,我们处理的是当前访问的节点,还是下一层需要访问的节点
这个决定了我们的终止条件的写法
"""
from typing import List
#如果处理的当前的节点:
def dfs(rooms:List[List[int]],key,visited:List[int]):
    #终止条件
    if visited[key]==True:  #本层递归是True,说明访问过
        return 
    
    #单层逻辑
    visited[key] = True
    for key in  rooms[key]:
        #继续深搜
        dfs(rooms,key,visited)

#如果是处理下一层节点的话
def dfs(rooms:List[List[int]],key,visited):
    #这时候就不需要终止条件,因为如果不满足条件,根本进不来
    for key in rooms[key]:
        if visited[key]==True:
            continue
        else:
            visited[key]=True
            dfs(rooms,key,visited)


"""
深搜整体代码
"""
class Solution():
    def canVisitAllRooms(self,rooms:List[List[int]])->bool:
        #初始化
        visited = [False]*len(rooms)

        def dfs(rooms,key,visited):
            for key in rooms[key]:
                if visited[key]==False:
                    visited[key]=True
                    dfs(rooms,key,visited)
        
        dfs(rooms,0,visited)
        visited[0] = True
        for val in visited:
            if val == False:
                return False
        return True 


"""
广搜整体代码,广搜就是一圈一圈搜索,不像深搜是一条路走到黑
"""
from collections import deque 
class Solution():
    def canVisitAllRooms(self,rooms:List[List[int]])->bool:
        visited = [False]*len(rooms)

        def bfs(rooms,key,visited):
            que = deque()
            que.append(key)
            visited[key]=True
            while que:
                key = que.popleft()
                for key in rooms[key]:
                    if visited[key]==False:
                        visited[key]=True
                        que.append(key)
        
        bfs(rooms,0,visited)

        for key in visited:
            if key==False:
                return False
        return True


if __name__=="__main__":
    solution = Solution()
    rooms = [[1],[2],[3],[0]]
    print(solution.canVisitAllRooms(rooms))