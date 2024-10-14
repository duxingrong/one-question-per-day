"""
给定不同面额的硬币和一个总金额,写出函数来计算可以凑成总金额的硬币组合数.假设每一种面额的硬币有无限个

这是一个完全背包求组合(这里求组合和排列是不一样的)

结论:求组合是外层遍历物品,而求排列是外层遍历背包
"""
"""
dp[j] 将容量j装满总共有dp[j]中组合数字
假如此时遍历到物品i: 如果不取,那就是dp[j],如果取,那就是dp[j-weight[i]],因为此时只需要考虑装满背包[j-weight[i]]有多少种方法了
所以第推公式:dp[j]+=dp[j-weight[i]]
初始化:dp[0]=1 没有实际意义,完全是dp第推公式的需要.
遍历顺序:因为是组合,所以先遍历
"""
from typing import List

class Solution():
    def change(self,target:int,coins:List[int])->int:
        #dp数组
        dp=[0]*(target+1)
        #初始化
        dp[0]=1
        for coin in coins:
            for j in range(coin,target+1):
                dp[j]+=dp[j-coin]
        return dp[target]

coins=[1,2,5]
target=11
solution=Solution()
print(solution.change(target,coins))
