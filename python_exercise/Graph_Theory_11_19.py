"""

Bellman_ford算法(优化)SPFA算法

某国为促进城市间经济交流，决定对货物运输提供补贴。共有n个遍号为1到n的城市，通过道路网络连接，网络中的道路仅允许从某个城市单向通行到另一个城市，不能反向通行
网络中的道路都有各自的运输成本和政府补贴，道路的权值计算方式为:运输成本和政府补贴
权值为正表示扣除了政府补贴后运输货物仍需要支付的费用，权值为负则表示政府的补贴超过了支出的运输成本，世纪表现为运输过程中还能赚取一定的收益

请找出从城市1到城市n的所有可能路径中，综合政府补贴后的最低运输成本
如果最低运输成本是一个负数，它表示在遵循最优路径的情况下，运输过程中反而能够实现盈利
城市1到城市n之间可能会出现没有路径的情况，同时保证道路网络中不存在任何负权回路

输入描述:
第一行包含两个正整数,第一个正整数n表示该国一共有n个城市，第二个整数m表示这些城市中共有m条道路
接下来的m行，每行包括三个整数，s,t和v,表示s号城市运输货物到t号城市,道路权值为v(单向图)

输出描述:
如果能够从城市1连通到城市n,请输出一个整数，表示运输成本。如果该整数是负数，则表示实现了盈利，如果从城市1没有路径可到达城市n，请输出'unconnected'

输入示例
6 7 
5 6 -2 
1 2 1
5 3 1 
2 5 2 
2 4 -3 
4 6 4 
1 3 5 

Bellman_ford算法每次松弛都是对所有的边进行松弛

但是真正有效的松弛，是基于已经计算过的节点在做的松弛

所以算法可以简化成：只需要对上一次松弛的时候更新过的节点作为出发节点所连接的边进行松弛就够了

并且用visited数组记录已经在队列里的元素，已经在队列中的元素不用重复加入

"""
from collections import deque

def Bellman_ford(graph,n):
    minDist= [float('inf')]*(n+1)
    visited= [False]*(n+1)
    que = deque()

    #节点1的minDist数组初始化为1
    minDist[1]=0
    que.append(1)
    visited[1]=True
    while que:
        cur = que.popleft()
        visited[cur]=False

        for t,val in graph[cur]:
            if minDist[cur]+val< minDist[t]:
                minDist[t]=minDist[cur]+val
                if visited[t]==False:
                    que.append(t)
                    visited[t] = True
                
    return minDist[n] if minDist[n]!=float('inf') else -1


if __name__=="__main__":
    n,m = map(int,input().split())
    edges = []

    for _ in range(m):
        edges.append(list(map(int,input().split())))

    graph = {i:[] for i in range(1,n+1) }

    #创建邻接表
    for s,t,val  in edges:
        graph[s].append([t,val])

    result = Bellman_ford(graph,n)
    if result!=-1:
        print(result) 
    else:
        print("unconnected")








        
