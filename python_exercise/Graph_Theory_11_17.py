"""
dijkstra(朴素版)

小明是一位科学家，他需要参加一场重要的国际科技大会，以展示自己的最新研究成果
小明的起点是第一个车站，终点是最后一个车站，然而，途中的各个车站之间的道路状况，交通拥堵程度以及可能的自然因素(如天气变化)等不同，这些因素都会影响每条路径的通行时间
小明希望选择一条花费时间最少的路线，以确保他能够尽快到达目的地

输入描述:
第一行包含两个正整数，第一个正整数N表示一共有N个公共汽车站，第二个正整数表示有M条公路
接下来M行，每行包括三个整数，S，E和V，代表了从S车站可以单向直达E车站，并且需要花费V单元的时间

输出描述:
输出一个整数，代表小明从起点到终点所花费的最小时间
"""

"""
本题目就是求最短路，最短路是图论中的经典问题即：给出一个有向图，一个起点，一个终点，问起点到终点的最短路径
dijkstra算法:在有权图(权值非负数)中求从起点到其他节点的最短路径算法
三部曲:
1. 选源点到哪个节点近且该节点没有被访问过
2. 该最近的节点被标记访问过
3. 更新非访问节点到源点的距离(即更新minDist数组)

minDist数组用来记录每一个节点距离源点的最小距离
"""

"""
prim和dijkstra的区别
二者的区别在于minDist数组
prim:      记录每个一个节点距离最小生成树的最小距离
dijkstra:  记录每一个节点距离源点的最小距离
prim是在无向图中找一条连通各节点的最短路径
dijkstra是在有向图中找起点到各个节点的最短路径
"""
import heapq
def dijkstra(edges,n):
    #使用邻接表提高效率
    graph = {i:[] for i in range(1,n+1)}
    for s,t,val in edges:
        graph[s].append([t,val])


    minDist = [float("inf")]*(n+1)
    visited = [False]*(n+1)
    min_heap = []

    minDist[1] = 0 #起点距离自己当然为0
    heapq.heappush(min_heap,(0,1)) 

    while min_heap:
        current_dist, node = heapq.heappop(min_heap)

        if visited[node]==True:
            continue  #因为就是一个最小堆，肯定会重复取出最小的，遍历过的pass

        visited[node]=True  #下面将处理该节点

        for neighbor,weight in graph[node] :
            if  visited[neighbor]==False:
                new_dist = weight+current_dist
                if new_dist < minDist[neighbor]:
                    minDist[neighbor]=new_dist #只有小于时候才用更新
                    heapq.heappush(min_heap,(new_dist,neighbor))#同时edge[1]距离起点的最短路径也要更新

    #如果有路径就返回最短距离，没有则返回-1
    return minDist[n] if minDist[n]!= float('inf') else -1


if __name__=="__main__":
    n,m = map(int,input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int,input().split())))
    result = dijkstra(edges,n)
    print(result)


