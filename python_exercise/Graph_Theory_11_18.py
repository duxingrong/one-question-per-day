"""
Bellman_ford算法

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
"""

"""

这个是找起点到终点的最短路径，在有向图中，不必通过所有城市,和dijkstra唯一的区别就是它可以有负权值，这个在dijkstra中是没有办法处理的,所以需要用到Bellman_ford
因为dijkstra算法的贪心思想就是假设当前已经找到的最短路径不会再被更新，负权边会破坏这种假设,如果存在更短的路径，但是最小堆已经处理过该节点，无法重新回溯进行更新

Bellman_ford算法的核心思想就是对所有边进行松弛n-1次操作(n为节点数量),从而求得目标最短路
还是用minDist数组来表达起点到各个节点的最短距离,松弛n-1次
为什么是n-1次?
因为对所有边松弛一次，相当于计算起点到达终点一条边相连的节点的最短距离,这里说的是一条边相连的节点
那么对所有边松弛n-1次，就相当于计算起点到达终点n-1条边的节点,也就是最远的节点都保证了,所以n-1次
"""

def Bellman_ford(graph,n):

    minDist= [float('inf')]*(n+1)
    minDist[1]=0
    for _ in range(n-1): #松弛n-1次
        update = False
        #将所有边刷新一次
        for s,t,val in graph:
            if minDist[s]!=float('inf') and minDist[s]+val< minDist[t]:
                minDist[t]=minDist[s]+val
                update=True
        #如果我松弛几次后就已经完全体了，因为我这一次松弛没发生任何更新,那就没必要继续松弛了
        if update == False:
            break

    #检查负权回路:第n次松弛如果还能更新，说明有负权回路
    for s,t,val in graph:
        if minDist[s]!=float('inf') and minDist[s]+val< minDist[t]:
            return "Negative weight cycle detected"

    #如果连通了，就是返回 
    return minDist[n] if minDist[n]!=float('inf')  else "unconnected"



if __name__=="__main__":
    n,m = map(int,input().split())
    graph = []
    for _ in range(m):
        graph.append(list(map(int,input().split())))

    result = Bellman_ford(graph,n)
    print(result)




