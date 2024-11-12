"""
有一个图，它是一棵树，他是拥有n个节点(节点编号1到n)和n-1条边的连通无环无向图(其实就是一个线形图)
现在在这棵树上的基础上，添加一条边(依然是n个节点,但有n条边)，使这个图变成了有环图
请你找出冗余边，删除后，使该图可以重新变成一棵树

输入描述:
第一行包含一个整数N，表示图的节点个数和边的个数
后续N行，每行包含两个整数s和t,表示图中s和t之间有一条边

输出描述:
输出一条可以删除的边，如果有多个答案，请删除标准输入中最后出现的那条边
"""

class UnionFind():

    def __init__(self,size):
        self.parent = list(range(size+1))

    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u==root_v:
            print(f"{u} {v}")
            return 
        else:
            self.parent[root_v]=root_u

    def find(self,u):
        if u == self.parent[u]:
            return u
        else:
            self.parent[u]=self.find(self.parent[self.parent[u]])
            return self.parent[u]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0 
    n  = int(data[index])
    uf = UnionFind(n)
    
    index+=1
    for _ in range(n):
        s = int(data[index])
        index+=1
        t = int(data[index])
        index+=1
        uf.union(s,t)
        
if __name__=="__main__":
    main()
