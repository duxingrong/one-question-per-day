"""
给定一个机票的字符串二维数组[from,to],子数组中的两个成员分别表示飞机出发和降落的机场地点,对该行程进行重新规划排序,所有这些机票都必须从JFK开始

如果存在多种有效的行程,按照字符自然排序返回最小的行程组合
所有的机场都用三个大写字母来表示
假定所有的机票至少存在一种合理的行程
所有的机票必须使用一次且只能使用一次

例如:
输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
"""

"""
经典的行程重建问题
1. 问题转化为图问题:
把每个机场看成图中的节点,每张机票表示节点之间的有向边.
从JFK出发,找到所有可能的行程,并且所有的票都要用一次
2. 字典顺序的要求:
由于需要按照字母自然顺序找到最小的行程,所以可以对每个机场的出发目的地按照字典顺序进行排序
3.DFS:
我们从JFK开始,用DFS去遍历图,并在每次访问到某个机场时,尝试按字典优先访问它能去的目的地
4.每条边只能使用一次:
这是一个欧拉路径问题,即从某个顶点出发,遍历每条边且每条边只访问一次
"""


"""
1: 对所有机票进行排序(这样字典里才会是按照小到大的顺序排列的),并且创建出来一个出发地对应目的地的字典
"""
from collections import defaultdict
from typing import List
class Solution():
    def __init__(self):
        self.graph = defaultdict(list) # 初始化字典
        self.result = []

    def findItinerary(self,tickets:List[List[str]]):
        # 首先是构建出映射的字典
        # 排序
        tickets=sorted(tickets,reverse=True) # 从大到小排列,这样pop()会比pop(0)的时间少很多
        for from_ ,to in tickets:
            self.graph[from_].append(to) #字典赋值
        # 调试:
        for key,value in self.graph.items():
            print(f"{key}:{value}")
        # 开始递归
        self.dfs("JFK")
        return self.result[::-1] # 从搜索逻辑可以看出,它是逆序,需要反转
    """
    2. 现在开始递归的逻辑,我们从JFK开始,按顺序去访问,然后递归,直到最后一个没有目的地去后,返回它本身,然后回溯加入result
    """
    def dfs(self,airport):
        # 取出当前机场的目的地列表
        while self.graph[airport]:
            next_airport = self.graph[airport].pop() #python中的列表拥有pop操作
            self.dfs(next_airport)

        # 递归终止的时候,将机场加入结果
        self.result.append(airport)
        
        

# 调试
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
solution =Solution()
print(solution.findItinerary(tickets))








