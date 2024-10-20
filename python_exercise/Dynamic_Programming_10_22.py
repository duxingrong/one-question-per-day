"""

给定一个整数数组prices,它的第i个元素prices[i]是一支给定的股票在第i天的价格,你最多可以完成k笔交易,注意:你不能同时参与多笔交易

那就是一样的套路,只不过是从最多两次到最多k次
dp[i][1]:第一次持有
dp[i][2]:第一次不持有
...
dp[i][2*k-1]: 第k次持有
dp[i][2*k]:第k次不持有
"""

from typing import List

class Solution():
    def maxProfit(self,k:int,prices:List[int])->int:
        if len(prices)==0:
            return 0
        #dp数组
        dp=[[0]*(2*k+1) for _ in range(len(prices))]
        #初始化
        for i in range(1,2*k+1,2):
            dp[0][i]=-prices[0]

        for i in range(1,len(prices)):
            for j in range(1,2*k+1):
                if j%2==1:#奇数是持有
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+prices[i])
        print(dp)
        return dp[-1][-1]


k=2
prices=[3,2,6,5,0,3]
result=Solution().maxProfit(k,prices)
print(result)


