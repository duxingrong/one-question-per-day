"""
2920.收集所有金币可获得的最大积分

有一棵由n个节点组成的无向树，以0为根节点，节点编号从0到n-1，给你一个长度为n-1的二维整数数组edges，其中edges[i]=[ai,bi],表示在树上的节点ai和bi之间存在一条边，另给你一个下标从0开始，长度为n的数组coins和一个整数k，其中coins[i]表示节点i处的金币数量。
从根节点开始，你必须收集所有金币，要想收集节点上的金币，必须先收集该节点的祖先节点上的金币

节点i上的金币可以用下述方法之一进行收集:
- 收集所有金币，得道共计coins[i]-k点积分，如果coins[i]-k是负数，你将会失去abs(coins[i]-k)点积分。
- 收集所有金币，得道共计floor(coins[i]/2)点积分,如果采用这种方法，节点i子树中所有节点j的金币数coins[j]将会减少至floor(coins[j]/2)。

返回收集所有树节点的金币之后可以获得的最大积分
"""

from functools import cache
from typing import List
"""
这里的难点其实就是在于，我们要记录下收集一半的次数(自上而下的时候),因为我们当前节点选择了第二种，会导致下面的所有节点的coins都变成一半，这个是会累加的

位运算，更简便的除一半的方法# coins[i]>>j == coins[i]/2^j


"""

class Solution:
    def maximumPoints(self,edges:List[List[int]],coins:List[int],k:int)->int:
        @cache
        def dfs(i:int,fa:int,j:int)->int: # 当前节点i,fa:节点i的父节点,j:减半的次数
            a = (coins[i]>>j)-k # coins[i]>>j == coins[i]/2^j
            b = (coins[i]>>(j+1))
            for c in g[i]:
                if c!= fa: # 防止死循环
                    a += dfs(c,i,j) # 递归去子节点
                    if j <14 : # 这是为了防止溢出
                        b+= dfs(c,i,j+1)
            return max(a,b) 

        n = len(coins)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = dfs(0,-1,0)
        dfs.cache_clear()
        return ans

"""
cache: 核心作用就是**记住以前做过的事情**,避免重复劳动，提升效率
只要计算出fib(3),就把它保存下来。下次用到fib(3)时，直接拿出来用，省去了重复计算
"""
from functools import cache

@cache
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(10)) # 快速计算，因为每个结果只计算一次


