"""
某国为促进城市间经济交流，决定对货物运输提供补贴。共有 n 个编号为 1 到 n 的城市，通过道路网络连接，网络中的道路仅允许从某个城市单向通行到另一个城市，不能反向通行。
网络中的道路都有各自的运输成本和政府补贴，道路的权值计算方式为：运输成本 - 政府补贴。权值为正表示扣除了政府补贴后运输货物仍需支付的费用；
权值为负则表示政府的补贴超过了支出的运输成本，实际表现为运输过程中还能赚取一定的收益。
然而，在评估从城市1到城市n的所有可能路径中的综合政府补贴沟的最低运输成本时，存在一种情况：图中可能出现负权回路
负权回路是指一系列道路的总权值为负，这样的回路使得通过反复经过回路中的道路，理论上可以无限的减少总成本或无限地增加总收益
请找出从城市 1 到城市 n 的所有可能路径中，综合政府补贴后的最低运输成本。同时能够检测并适当处理负权回路的存在。
城市 1 到城市 n 之间可能会出现没有路径的情况

【输入描述】

第一行包含两个正整数，第一个正整数 n 表示该国一共有 n 个城市，第二个整数 m 表示这些城市中共有 m 条道路。

接下来为 m 行，每行包括三个整数，s、t 和 v，表示 s 号城市运输货物到达 t 号城市，道路权值为 v。

【输出描述】

如果没有发现负权回路，则输出一个整数，表示从城市 1 到城市 n 的最低运输成本（包括政府补贴）。

如果该整数是负数，则表示实现了盈利。如果发现了负权回路的存在，则输出 "circle"。如果从城市 1 无法到达城市 n，则输出 "unconnected"。
"""

from collections import deque,defaultdict
"""
在极端情况下，所有的节点都与其它节点相连，每个节点的入度都为n-1,所以每个节点最多加入n-1次队列
如果超过了这个值，那么图中一定存在负权回路
"""
def SPFA(graph,n):
    minDist= [float('inf')]*(n+1) #用来记录最短路径
    visited = [False]*(n+1) #用来记录是否入列
    count = [0]*(n+1)  #用来判断是否有环
    queue = deque()

    #初始化
    minDist[1]=0
    queue.append(1)
    count[1]+=1
    visited[1]=True

    while queue:
        cur = queue.popleft()
        visited[cur]=False
        for t,val  in graph[cur]:
            if minDist[cur]+val <minDist[t]:
                minDist[t]= minDist[cur]+val
                queue.append(t)
                count[t]+=1
                #判断是否超出n-1
                if count[t]==n:
                    return -2

    return minDist[n] if minDist[n]!=float('inf') else -1


if __name__=="__main__":
    #n个城市，m条道路
    n,m = map(int,input().split())

    graph = defaultdict(list)

    #邻接表储存道路
    for _ in  range(m):
        s,t,val= map(int,input().split())
        graph[s].append([t,val])

    result= SPFA(graph,n)

    if result==-2:
        print("circle")
    elif result ==-1:
        print("unconnected")
    else:
        print(result)




    

