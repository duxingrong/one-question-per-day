"""
给定一个数组,它的第i个元素是一支给定的股票在第i天的价格
你最多可以进行两笔交易,你不能同时参与多笔交易,你必须在再次购买前出售之前的股票
"""

"""
唯一的区别变成了最多进行两次交易(这个怎么判断呢?)
所以这个题目的每一天变成了有4种状态

dp[i][1]:第一次持有的最大现金
dp[i][2]:第一次不持有的最大现金这里特指的是卖出后的不持有,不包括最开始的无操作
dp[i][3]:第二次持有的最大现金
dp[i][4]:第二次不持有的最大现金
第推:
dp[i][1]:max(dp[i-1][1],-prices[i])
dp[i][2]:max(dp[i-1][2],dp[i-1][1]+prices[i])
dp[i][3]:max(dp[i-1][3],dp[i-1][2]-prices[i])
dp[i][4]:max(dp[i-1][4],dp[i-1][3]+prices[i])
初始化:
dp[0][1]=-prices[0]
dp[0][2]=0
dp[0][3]=-prices[0] 你就理解为买了,当天卖出,然后又买了(虽然和现实不符合)
dp[0][4]=0
"""

from typing import List

class Solution():
    def maxProfit(self,prices:List[int])->int:
        if len(prices)==0:
            return 0

        dp=[[0]*5 for _ in range(len(prices))]
        dp[0][1]=dp[0][3]=-prices[0]

        for i in range(1,len(prices)):
            dp[i][1]=max(dp[i-1][1],-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        print(dp)
        return dp[-1][4] #可以理解为哪怕dp[-1][2]是最大的,但是我可以当天买当天卖,这样dp[-1][4]一定包括了dp[-1][2]
