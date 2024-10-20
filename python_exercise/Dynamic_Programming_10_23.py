"""
给定一个整数数组,其中第i个元素代表了第i天的股票价格,你可以多次买卖一支股票
你不能同时参与多笔交易
卖出股票后，你无法在第二天买入股票(冷却期为1天)

和前面的相比,唯一区别就是有冷却期
这里的难点就是要把不持有股票的状态继续拆分成 保持不持有 当天卖出  冷却期
每天一共就这四中状态:
dp[i][0]:持有股票的最大现金
dp[i][1]:保持不持有的最大现金
dp[i][2]:具体卖出的最大现金
dp[i][3]:冷却期的最大现金

第推:
dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])
dp[i][1]=max(dp[i-1][1],dp[i-1][3])
dp[i][2]=dp[i-1][0]+prices[i]
dp[i][3]=dp[i-1][2]
如何初始化呢?
这种最好是用第2天来反推第一天,或者你这么理解，我剩下三种加一起就是不持有，那就是都初始化为0
dp[0][0]=-prices[0]
dp[0][1]=0
dp[0][2]=0
dp[0][3]=0
"""

from typing import List

class Solution():
    def maxProfit(self,prices:List[int])->int:
        if len(prices)==0:
            return 0
        #dp数组
        dp=[[0]*4 for _ in range(len(prices))]
        #dp初始化
        dp[0][0]=-prices[0]
        dp[0][1]=0
        dp[0][2]=0
        dp[0][3]=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i],dp[i-1][3]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]
        print(dp)
        return max(dp[-1][1],dp[-1][2],dp[-1][3])

prices=[1,2,3,0,2]
solution=Solution()
print(solution.maxProfit(prices))
