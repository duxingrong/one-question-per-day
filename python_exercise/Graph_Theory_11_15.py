"""
在世界的某个区域，有一些分散的神秘岛屿，每个岛屿上都有一种珍稀的资源或者宝藏，国王打算在这些岛屿上建公路，方便运输

不同岛屿之间，路途距离不同，国王希望你可以规划建公路的方案，如何可以用最短的总公路距离将所有岛屿连通起来

输入描述:
第一行包含两个整数V和E，V代表顶点数，E代表边数。顶点编号是从1到V。
接下来的E行，每行三个整数v1,v2,val ,v1和v2为边的起点和终点，val代表边的权值

输出描述:
输出联通所有岛屿的最小路径总距离

kruskal算法
1. 边的权值排序，因为要优先选最小的边加入到生成树里
2. 遍历排序后的边.
    如果边首尾的两个节点在同一个集合，说明如果连上这条边图中会出现环
    如果边首尾的两个节点不在同一个集合，加入到最小生成树，并把两个节点加入到同一个集合中

区别:

prim算法是维护节点的集合，而kruskal是维护边的集合

节点多，边少，用prim

节点少，边多，用kruskal

"""

import heapq
class UnionFind():

    def __init__(self,size):
        self.parent = list(range(size+1))
        self.min_heapq = []
        self.result = 0

    def find(self,u):
        if u == self.parent[u]:
            return u
        else:
            self.parent[u]=self.find(self.parent[u])
            return self.parent[u]

    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u==root_v:
            return 
        self.parent[root_v]=root_u

    def isSame(self,u,v):
        return self.find(u)== self.find(v)


        
    def getstart(self,edges):
        for edge in edges:
            heapq.heappush(self.min_heapq,(edge[2],edge))
        while self.min_heapq:
            edge = heapq.heappop(self.min_heapq)[1]
            if self.isSame(edge[0],edge[1]):
                continue
            else:
                self.union(edge[0],edge[1])
                self.result+=edge[2]
        return self.result


if __name__=="__main__":
    n,e = map(int,input().split())
    edges = []

    for _ in range(e):
        s,t,val = map(int,input().split())
        edges.append([s,t,val])

    uf = UnionFind(n)

    result = uf.getstart(edges)
    print(result)
        
        
