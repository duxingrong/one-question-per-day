"""

冗余连接

树可以看成是一个连通且无环的无向图

给定往一棵n个节点(节点值1~n)的树中添加一条边后的图.添加的边的两个顶点包含在1到n中间,且这条附加的边不属于树中已存在的边.图的信息记录于长度为n的二维数组edges,edges[i]=[ai,bi],表示图中ai和bi之间存在一条边

请找出一条可以删去的边,删除后可使得剩余部分是一个有着n个节点的树,如果有多个答案,则返回数组edges中最后出现的边



这是并查集的基础
并查集的作用:判断两个节点在不在一个集合,也可以将两个节点添加到一个集合中

"""

class UnionFind():
    def __init__(self,size):
        #初始化每个节点的父集都是自己
        self.parent = list(range(size+1))

    # 查找父节点(递归)
    def find(self,node):
        if self.parent[node]==node:
            return node
        else: #路径压缩
            self.parent[node]=self.find(self.parent[node])
            return self.parent[node]

    # 将u,v添加入到一个集合
    def union(self,u,v):
        root_u= self.find(u)
        root_v = self.find(v)
        if root_u==root_v: #已经在就不用操作了
            return 
        self.parent[root_v]=root_u

    # 判断是否在一个并查集
    def isSame(self,u,v):
        return self.find(u)==self.find(v)



from typing import List

class Solution():
    def findRedundantConnection(self,edges:List[List[int]])->List[int]:
        n = len(edges)
        #实例化
        uf = UnionFind(n)
        for edge in edges:
            if not uf.isSame(edge[0],edge[1]):
                uf.union(edge[0],edge[1])
            else:
                return edge
        
        return []
        

    




    



