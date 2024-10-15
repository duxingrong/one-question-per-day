"""
假设你正在爬楼梯.需要n阶才能到楼顶
每次你可以爬至多m个台阶(1<=m<n),你有多少种不同的方案可以爬到楼顶呢?
这完全就是完全背包套了一层壳.翻译过来就是容量为n的背包用m个物品,有多少种方法可以装满

"""
"""
dp[j]到j阶梯有dp[j]种不同的方法
dp[j]+=dp[j-weight]
由第推公式得出dp[0]=1
是排列.所以外层背包,内层物品
"""
from typing import List

class Solution():
    def function(self,n:int,m:int)->int:
        # dp数组
        dp=[0]*(n+1)
        #初始化
        dp[0]=1
        #遍历(先背包,后物品,顺序)
        for j in range(1,n+1):
            for weight in range(1,m+1):
                if j>=weight:
                    dp[j]+=dp[j-weight]
                    print(dp)

        return dp[n]

n=3
m=2
solution=Solution()
print(solution.function(n,m))





