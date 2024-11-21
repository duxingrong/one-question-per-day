"""

bellman_ford之单源有限最短路

某国为促进城市间经济交流，决定对货物运输提供补贴。共有n个编号为1到n的城市，通过道路网络连接，网络中的道路仅允许从某个城市单向通行到另一个城市，不能反向通行

网络中的道路都有各自的运输成本和政府补贴，道路的权值计算方式为:运输成本-政府补贴。

权值为正表示扣除了政府补贴后运输货物仍然需要支付的费用;
权值为负则表示政府的补贴超过了支出的运输成本，实际表现为运输过程中还能赚到一定的收益

请计算最多经过k个城市的条件下，从城市src到城市dst的最低运输成本


输入描述:
第一行包含两个正整数，第一个正整数n表示该国一共有n个城市，第二个整数m表示这些城市中央有m条道路

接下来的m行，每行包括三个整数，s,t,和v,表示S号城市运输货物到t号城市，道路权值为v

最后一行包含三个正整数,src,dst,和k，src和dst为城市编号,从src到dst经过的城市数量限制为k

输出描述:
输出一个整数，表示从城市src到城市dst的最低运输成本，如果无法在给定经过城市数量的限制下找到从src到dst的路径，则输出'unreachable',表示不存在符合条件的运输方案


本题目相当于从起点最多经过k+1条边到达终点的最短距离

这个题目的关键在于如何才能限制k+1次呢？bellman_ford算法本质上没有限制边数的能力

理论上来说，对所有边松弛一次，相当于一定计算出起点到达起点一条边相连的节点的最短距离,以此类推
但是并不是说每一轮就一定不会超过这个一条边的距离,有可能你在第一轮中，就更新了4个节点走到了终点的距离,这个意思就是，本质上bellman_ford算法没法限制住最做经过(在有负权回路的情况下)

那我们该怎么捆绑呢？让它严格满足每一轮，只能最多松弛到达起点一条边的距离
用上一轮的minDist就可以,这里我们需要知道为什么会出现多更新的情况，就是因为当前更新了节点2后，如果下一条边是2->3，那这一轮就又会更新节点3了，相当于第一轮却更新了到达起点2条边的最短距离,但是如果用上一轮的minDist,那此时的minDist[2]

"""

from collections import defaultdict

def bellman_ford(graph,n,k,src,dst):

    minDist= [float('inf')]*(n+1)  #记录每个节点距离起点的最小距离
    minDist[src]=0



    for _ in range(k+1):
        #用上一轮的来更新才对
        minDist_copy = minDist.copy() #不能直接赋值，因为是同一块内存
        for i in range(1,n+1):
            if graph[i] and minDist_copy[i]!=float('inf'):
                for t,v in graph[i]:
                    if minDist[t]>minDist_copy[i]+v:
                        minDist[t]=minDist_copy[i]+v

    return minDist[dst] if minDist[dst]!=float('inf') else 'unreachable'


if __name__=="__main__":

    n,m = map(int,input().split())

    #创建邻接表
    graph = defaultdict(list)
    for _ in range(m):
        s,t,v = map(int,input().split())
        graph[s].append([t,v])
    
    src, dst,k= map(int,input().split())

    #创建一个函数，它只需要松弛k+1次
    result = bellman_ford(graph,n,k,src,dst)
    print(result)
    
    


