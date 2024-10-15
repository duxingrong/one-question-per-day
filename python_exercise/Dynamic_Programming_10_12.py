"""
给定不同的硬币coins和一个总金额amount,编写一个函数来计算可以凑成总金额的最少硬币个数.如果没有任何一种硬币组合能组成总金额,返回-1

dp[j],凑满容量j的最少个数是dp[j]
是组合,所以外层物品,内层背包,完全背包:顺序
当遍历到物品i的时候:
里面遍历到背包j:
此时两种选择:如果不加入这个物品的最少个数,就是dp[j](滚动数组,此时的这个dp[j]是二维的dp[i-1][j],也就相当于此时等于从物品0到i-1中装满的最少个数),如果选择这个物品,那dp[j]=dp[j-weight]+1.等于将容量j-weight装满后加上当前这个物品,就是装满的个数
然后两者取最小值,就是dp[j]
所以dp[j]=min(dp[j],dp[j-weight]+1)
所以整体初始化成['inf']*(背包容量+1),而dp[0]=0,才能满足公式
"""
from typing import List

class Solution():
    def coinChange(self,coins:List[int],amount:int):
        #dp数组
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j]=min(dp[j],dp[j-coin]+1)

        if dp[amount]==float('inf'):
            return -1
        return dp[amount]


