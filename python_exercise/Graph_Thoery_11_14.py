"""
题目描述：
在世界的某个区域，有一些分散的神秘岛屿，每个岛屿上都有一种珍稀的资源或者宝藏。国王打算在这些岛屿上建立公路，方便运输
不同岛屿之间，路途距离不同，国王希望你可以规划公路的方案，如何可以以最短的总公路距离将所有岛屿连通起来。
输入描述:
第一行包含两个整数V和E，V代表顶点数，E代表边数。顶点编号是从1到V。例如V=2,一共有两个顶点，分别是1和2
接下来共有E行，每行三个整数v1,v2和val,v1和v2为边的起点和终点，val代表边的权值
输出描述:
输出联通所有岛屿的最小路径总距离
7 11 
1 2 1
1 3 1 
1 5 2 
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2 
5 7 1
6 7 1

6
"""

"""
首先要明确，它是一个无向图,换句话说找的是连接所有岛屿的公路(只需要保证每个岛屿都联通即可)
是最小生成树的模板题目,即所有节点的最小连通子图，即：以最小的成本(边的权值)将图中所有节点连接到一起
图中有n个节点，那么一定可以用n-1条边将所有的节点连接到一起，如何选择这n-1条边就是最小生成树算法所在
prim算法的核心就是三步:
1. 选距离生成树最近节点
2. 最近节点加入生成树
3. 更新非生成树节点到生成树的距离(即更新minDist数组)

minDist数组用来记录每一个节点距离最小生成树的最近距离,初始化为最大的节点距离就好
我们根据minDist数组，选取距离生成树最近的节点加入生成树，那么minDist数组里记录的其实也是最小生成树的边的权值

"""
#引入最小堆
import heapq
class Prim():
    def __init__(self,size):
        #都从1开始有效
        self.minDist = [10001]*(size+1) 
        self.visited = [False]*(size+1)
        self.result =0

    #有一个函数来更新minDist数组
    def update(self,edges,node):
        self.visited[node]=True  #加入生成树
        #遍历所有的边，更新数组,要确保所有的和当前节点有关的边都得到更新,是无向图
        for edge in edges:
            if edge[0]==node and self.visited[edge[1]]==False:
                self.minDist[edge[1]]=min(edge[2],self.minDist[edge[1]])
            elif edge[1]==node and self.visited[edge[0]]==False:
                self.minDist[edge[0]]=min(edge[2],self.minDist[edge[0]])

    #一个函数来找出下一个最近的非树节点
    def findnode(self):
        min_heap = []
        for i in range(1,len(self.minDist)):
            if not self.visited[i]:
                #堆默认是一个最小堆，会根据第一个元素来排序
                heapq.heappush(min_heap,(self.minDist[i],i))

        if min_heap:
            return heapq.heappop(min_heap)[1] #返回最小节点的索引
        return None


    #一个函数得出结果
    def getresult(self,edges,start_node):
        self.minDist[start_node]=0 #从起点节点开始，初始化最短距离为0
        self.update(edges,start_node)
        nextnode = self.findnode()
        while nextnode:
            self.update(edges,nextnode)
            nextnode = self.findnode()

        #得到结果
        for i in range(1,len(self.minDist)):

            self.result+=self.minDist[i]
        return self.result

       


if __name__=="__main__":
    #接受数据
    V,E = map(int,input().split())
    edges = []
    for _ in range(E):
        s,t,val = map(int,input().split())
        edges.append([s,t,val])

    prim =Prim(V)
    #随便开始，这里从1
    result = prim.getresult(edges,1)
    print(result)
   



