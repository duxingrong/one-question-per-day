"""
给定一个有向图，包含N个节点，节点编号分别为1,2,...,N,现在从1号节点开始，如果可以从1节点到达任何节点，则输出1，否则输出-1

输入描述:
第一行包含两个正整数，表示节点数量N和边的数量K，口后序K行，每行两个整数s和t,表示从s节点有一条边单向连接到t节点

输出描述:
如果可以从1号节点到任何节点，输出1,否则输出-1

这里关键要想到递归的终止条件，我们深度搜索，是一条路走到黑，所以如果我们搜索的时候发现这个节点之前已经搜索过了，那就是没必要继续搜索了，因为这个节点相关的搜索一定之前搜索成了.这就是终止条件

"""


class Solution():
    def __init__(self):
        self.table = {}
        self.visited=set() #用来记录遍历过的所有节点


    def dfs(self,node):
        self.visited.add(node)
        #如果这个节点有路
        if node in self.table:
            for neighbor in self.table[node]:
                if neighbor not in self.visited: #如果指向的新节点没有遍历过，就记录，然后去遍历
                    self.visited.add(neighbor)
                    self.dfs(neighbor)

    
    def main(self):
        #填充字典
        n,m = map(int,input().split())
        for _ in range(m):
            s,t = map(int,input().split())
            if s not in self.table:
                self.table[s]=[]
            self.table[s].append(t)
        # for key,val in self.table.items():
        #     print(f"{key}:{val}")

        self.dfs(1) #从1开始

        #判断结果
        if len(self.visited)==n:
            print(1)
        else:
            print(-1)



solution =Solution()
solution.main()
       

