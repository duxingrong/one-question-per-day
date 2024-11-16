"""
拓扑排序
某个大型软件项目的构建系统拥有N个文件,文件编号从0到N-1,在这些文件中，某些文件依赖于其他文件的内容，这意味着如果文件A依赖于文件B，则必须在处理文件A之前处理文件B，清编写一个算法，用于确定文件处理的顺序

输入描述:
第一行输入两个正整数N，M，表示N个文件之间有M条依赖关系
后续M行,每行两个正整数S和T，表示T文件依赖于S文件

输出描述:
输出共一行，如果能处理成功，则输出文件顺序，用空格隔开
如果不能处理成功(相互依赖),则输出-1
5 4 
0 1 
0 2 
1 3 
2 4 
0 1 2 3 4 

拓扑排序是专门用来解决这类依赖的问题的,概括来说:给出一个有向图，把这个有向图转成线性的排序就叫做拓扑排序

当然拓扑排序也要检查这个有向图是否有环，即存在循环依赖的情况，因为这种情况时不能做线性排序的

所以拓扑排序也是图论中判断有向无环图的常用方法

具体方法:(BFS) dfs也可以，但是不是重点
1. 找到入度为0的节点，加入结果集
2. 将该节点从图中移除
用字典来统计依赖，用数组来记录文件的入度
"""

from collections import deque,defaultdict

def topological_sort(n,edges):
    isdegree = [0]*n #用来记录每个文件的入度
    umap = defaultdict(list) #用来记录依赖
    result = []

    for edge in edges:
        s,t = edge
        isdegree[t]+=1
        umap[s].append(t)

    que = deque([i for i in range(n) if isdegree[i]==0]) #将入度为0的文件加入队列

    while que: #将加入结果的节点和它所带来的入度全部删去
        cur = que.popleft()
        result.append(cur)
        for file in umap[cur]:
            isdegree[file]-=1
            if isdegree[file]==0:
                que.append(file)

    if len(result)==n:
        print(" ".join(map(str,result))) 
    else:
        print(-1) #有环
        

if __name__=="__main__":
    n,m = map(int,input().split())
    edges = tuple(map(int,input().split()) for _ in range(m))
    topological_sort(n,edges)

