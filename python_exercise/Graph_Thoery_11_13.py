"""
有一种有向树，该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点,而根节点没有父节点。有向树拥有n个节点和n-1条边.
现在有一个有向图，有向图是在有向树中添加了一条多余的边，请返回一条可以删除的边，使得删除该边之后该有相向图可以被当作一棵有向树
输入描述:
第一行输入一个整数N,表示有向图中节点和边的个数
后续N行，每行输入两个整数s和t，代表这是s节点连续并指向t节点的单向边
输出描述:
输出一条可以删除的边，若有多条边可以删除，请输出标准输入中最后出现的一条边
"""

"""
区别:
无向图:无向图中的环是由一组节点相互连通形成的,无论边的方向如何，只要从某个节点出发,能通过多条边回到该节点，就构成了一个环
有向图:有向图中的环必须是有方向性的，只有沿着边的方向从一个节点出发在返回该节点,才形成有向环,这要求图中的节点的指向性遵循从起点到终点的顺序


无相图检测冗余边的时候，只需要判断新加入的边是否连接了一个已经相连的两个节点,即检测两个端点是否属于同一个集合。一般可以使用并查集结构来检测无向图中的冗余边

有向图: 在有向图中，仅通过并查集判断两个节点是否属于同一个集合是不够的，因为并查集本身不考虑边的方向，解决有向图的冗余连接问题，通常需要考虑环内的方向性或借助拓扑排序来判断是否形成有向环

有向图：有向树要求除了根节点外的每个节点都有且只有一个父节点，这意味着每个节点的入度不能超过1
如果有向图中某个节点的入度为2,则多出来的一条入边也可能是冗余边，而不仅仅是环的问题，所以在有向图冗余连接的判定时，既要考虑入度是否大于1,也要考虑有向环的存在

步骤:
1. 检查入度为2的节点，判断那条边是冗余的
2. 如果没有入度2.检测有向环
3. 删除边的优先级，如果有入度为2的节点，优先删除其中一条入边,如果没有入度为2的节点，那么删除最后一条导致环形成的边
"""

from collections import defaultdict

class Solution():
    def __init__(self,size):
        self.parent = list(range(size+1))

    #需要用到并查集
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u==root_v:
            return 
        self.parent[v]=u

    def find(self,u):
        if u == self.parent[u]:
            return u
        self.parent[u]=self.find(self.parent[u])
        return self.parent[u]

    def isSame(self,u,v):
        return self.find(u)==self.find(v)

    #判断删除入度为2的一条边后，剩下的是不是有向树
    def is_tree_after_remove_edge(self,edges,edge):
        for i in range(len(edges)):
            if edges[i]==edge:  #我们的目的是看剩下的边是否是有向树，所以这条冗余边要跳过
                continue
            #判断是否是有向树，只要看是否是同一个集合
            s,t = edges[i]
            if self.isSame(s,t):
                return False
            else:
                self.union(s,t)
        return True
        
    #如果发现没有入度为2的节点，那就说明这个图本身就有环,所以我们要找到有环的边，这里只需要按顺序去并查集就好，因为有向树就是可以用并查集特殊处理
    def get_remove_edge(self,edges):
        for i in range(len(edges)):
            s,t = edges[i]
            if self.isSame(s,t):
                print(f"{s} {t}")
                return 
            else:
                self.union(s,t)
        
if __name__ == "__main__":
    n = int(input())
    edges = []
    in_degree = defaultdict(int)

    for i in range(n):
        s,t = map(int,input().split())
        edges.append([s,t])
        in_degree[t]+=1

    #寻找入度为2的边，并记录下标
    vec = []
    #倒序,因为如果两条边删除哪一条都可以，就要优先删除后面的
    for i  in range(len(edges)-1,-1,-1):
        if in_degree[edges[i][1]]==2:
            vec.append(edges[i])


    uf = Solution(n)
    #如果存在入度为2
    if len(vec)>0:
        if uf.is_tree_after_remove_edge(edges,vec[0]):  #这里因为只有一条冗余边，所以vec最多只有两个数，如果第一个删去后是有向树，就对了，否则直接删除第二个
            s,t = vec[0]
            print(f"{s} {t}")
        else:
            s,t = vec[1]
            print(f"{s} {t}")

    else:
        uf.get_remove_edge(edges)


