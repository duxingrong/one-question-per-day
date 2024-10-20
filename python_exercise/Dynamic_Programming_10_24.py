"""
给定一个整数数组prices,其中第i个元素代表了第i天的股票价格,非负整数fee代表了交易股票的手续费用
你可以无限次的完成交易,但是你每笔交易都需要付手续费,如果你已经购买了一个股票,在卖出它之前不能再继续购买股票了

唯一的区别就是他增加了手续费

"""

from typing import List

class Solution():
    def maxProfit(self,prices:List[int],fee:int)->int:
        if len(prices)==0:
            return 0
        #dp数组
        dp=[[0]*2 for _ in range(len(prices))]
        #初始化
        dp[0][0]=-prices[0]
        dp[0][1]=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)  #多了手续费而已

        return dp[-1][-1]


prices=[1,3,2,8,4,9]
fee=2

solution=Solution()
print(solution.maxProfit(prices,fee))








