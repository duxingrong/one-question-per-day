"""
在象棋中，马和象的移动规则分别是"马走日和象走田".现在给定骑士的起始坐标和目标坐标,要求根据骑士的移动规则，计算从起点到达目标点所需要的最短步骤
骑士移动规则如图，红色是起始位置，黄色是骑士可以走的地方(骑士走目)


输入描述:
第一行包含一个整数n,表示测试用例的数量
接下来的n行，每行包含四个整数a1,a2,b1,b2,分别表示骑士的起始位置(a1,a2)和目标位置(b1,b2)

输出描述:
输出共n行，每行输出一个整数，表示骑士从起点到目标点的最短步骤

本题目用BFS的A*算法
A*算法通过启发式函数，影响队列里元素的排序，每个节点的权值F = G+H
G: 起点到达目前遍历节点的步数
H: 目前遍历的节点到达终点的距离

通过欧拉距离计算两点之间的距离 d = sqrt((x1-x2)^2 + (y1-y2)^2)
x1,x2为起点坐标 ,y1,y2为终点坐标 ,abs为求绝对值, sqrt为求开根号
保证每次出队列，就是F最小的节点

A*算法搜的路径如何，完全取决于启发式函数怎么写
A*算法并不能保证一定是最短路，要考虑时间效率与准确度之间的一个权衡
游戏开发中,保证运行效率的情况下，A*算法中的启发式函数设计往往不是最短路，而是接近最短路的次短路设计
A*算法只适合于给出明确的目标找最短路径，多个目标的话不适合
"""
import heapq

def Astar(a1,a2,b1,b2):
    #元组才能当key
    start=(a1,a2)
    end = (b1,b2)
    if start == end:
        return 0
    dir = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

    #欧拉距离
    def distance(a,b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

    #q存放的是F=G+H，以及节点
    q =[(distance(start,end)+0,start)] 
    #通过字典记录每走到一个节点所花费的步数
    step = { start : 0}
    while q:
        d , cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        for  i  in range(8):
            #下一步跳的节点
            new = (cur[0]+dir[i][0],cur[1]+dir[i][1])
            if 1<=new[0]<= 1000 and 1<= new[1]<=1000:
                step_new = step[cur]+1
                #同一个节点，有可能通过不同的步数到达，要更新
                if step_new<step.get(new,float('inf')):
                    step[new]=step_new
                    #距离加上步数，就是权重
                    heapq.heappush(q,(distance(new,end)+step_new,new))

    return False



if __name__=="__main__":
    n =int(input())
    for  _ in range(n):
        a1,a2,b1,b2 = map(int,input().split()) 
        result = Astar(a1,a2,b1,b2)
        print(result)



