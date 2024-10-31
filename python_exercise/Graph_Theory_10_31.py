"""
给定一个有n个节点的有向无环图，节点编号从1到n，请编写一个函数，找出并返回所有从节点1到节点n的路径，每条路径应以节点编号的列表形式表示

输入描述:
第一行包含两个整数N,M，表示图中拥有N个节点，M条边,后续M行，每行包含两个整数s和t,表示图中的s节点与t节点中有一条路径

输出描述:
输出所有的可达路径，路径中所有节点的后面跟一个空格，每条路径独占一行，存在多条路径，路径输出的顺序可以任意

如果不存在任何一条路径，则输出-1.

注意输出的序列中，最后一个节点后面没有空格！

深搜三部曲:
1.确认递归函数，参数
首先我们dfs函数一定要存一个图，用来遍历的，需要存一个目前我们遍历的节点，定义为x。
还需要存一个n，表示终点，我们遍历的时候，用来判断x==n时候标明找到了终点

2. 确认终止条件
当目前遍历的节点为最后一个节点n的时候，就找到了一条从出发点到终点的路径
3.处理目前搜索节点出发的路径
for i in range(1,n+1): //遍历节点x链接的所有节点
    if graph[x][i]=1:  //找到x链接的节点
        path.append(i) //遍历到的节点加入到路径中来
        dfs(graph,i,n) //进入下一层递归
        path.pop()     //回溯，撤销本节点
"""

"""
邻接矩阵写法
map函数进行的是类型的转换
map(int ,input().split()) 是将输入的字符串按空格划分，然后转化成整型
"""

def dfs(graph,x,n,path,result):
    #终止条件
    if x==n: #说明找到一条路
        result.append(path.copy())
        return 
    #递归逻辑
    for i in range(1,n+1):
        if graph[x][i]==1: 
            path.append(i)
            dfs(graph,i,n,path,result)
            path.pop() #没有找到或者找万后，需要回溯来重新寻找

def main():
    n,m= map(int,input().split())
    graph= [[0]*(n+1) for _ in range(n+1)]
    
    #开始赋值
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a][b]=1

    #初始化
    result = []
    #由于题目是从节点1找到所有到节点5的路径 ,paht自带一个[1]，表示起点

    #开始深搜
    dfs(graph,1,n,[1],result)

    #判断结果
    if not result:
        print(-1)
    else:
        for path in result:
            print(" ".join(map(str,path))) #map(str,path) 将[1,2,3,4]变成['1','2','3','4']然后用空格连接
        
if __name__=="__main__":
    main()


"""
使用邻接表
"""
from collections import defaultdict

class Solution():
    def __init__(self):
        self.path=[]
        self.result = []

    def dfs(self,graph,x,n):
        if x==n:
            self.result.append(self.path.copy())
            return
        for i in graph[x]:
            self.path.append(i)
            self.dfs(graph,i,n)
            self.path.pop()

    def main(self):
        n,m = map(int,input().split())

        #创建邻链表
        graph = defaultdict(list)  #它可以为不存在的健创建空列表，

        for _ in range(m):
            s,t = map(int,input().split())
            graph[s].append(t)

        self.path.append(1)#已经确定是从1开始的
        self.dfs(graph,1,n)

        if not self.result:
            print(-1)
        for ans in self.result:
            print(" ".join(map(str,ans)))

if __name__=="__main__":
    solution=Solution()
    solution.main()

