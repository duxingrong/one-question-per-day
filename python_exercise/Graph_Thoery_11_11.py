"""
给定一个包含n个节点的无向图，节点编号从1到n
你的任务是判断是否有一条从节点source出发到节点destination的路径存在

输入描述:
第一行包含两个正整数N和M，N代表节点的个数，M代表边的个数
后序M行，每行两个正整数s和t，代表从节点s与节点t之间有一条边
最后一行包含两个正整数,代表起始节点source和目标节点destination

输出描述:
输出一个整数，代表是否存在从节点source到节点destination的路径。如果存在输出1,否则，输出0


路径和集合的关系:在这个问题中，判断从节点source到节点destination是否有路径，实际上等价于判断source和destination是否属于同一个连通分量,换句话说，如果这两个节点在同一个集合中，那么它们之间一定存在一条路径
"""


class UnionFind():
    def __init__(self,size):
        self.parent = list(range(size+1)) #初始化数组

    #查找节点的根节点并且进行路径压缩
    def find(self,u):
        if u == self.parent[u]: #他就是根节点
            return u
        else:
            self.parent[u]=self.find(self.parent[u]) #路径压缩
            return self.parent[u]

    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u==root_v:
            return 
        self.parent[root_v]=root_u

    def isSame(self,u,v):
        return self.find(u)==self.find(v)


def main():
    import sys
    input = sys.stdin.read #相当于一次性读取标准输入的全部内容,直到遇见EOF文件结束符
    data = input().split()

    index = 0
    n= int(data[index])
    index+=1
    m = int(data[index])
    index+=1

    #实例化类
    uf = UnionFind(n)

    for _ in range(m):
        s = int(data[index])
        index+=1
        t = int(data[index])
        index+=1
        uf.union(s,t)

    source = int(data[index])
    index+=1
    destination= int(data[index])

    if uf.isSame(source,destination):
        print(1)
    else:
        print(0)
    
if __name__ == "__main__":
    main()


