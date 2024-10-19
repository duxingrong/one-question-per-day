"""
给定一个数组,它的第i个元素是一支给定股票第i天的价格,你可以尽可能的完成多次交易,但是你不能同时参与多笔交易,再次购买前必须抛售出去

输入:[7,1,5,3,6,4]
输出:7
"""

"""
有了上一提的铺垫,那这题目唯一的区别就是可以进行多次交易
dp[i][0]:第i天持有该股票的最大现金  dp[i][1]:第i天不持有该股票的最大现金
第推
dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i]) 继承过来的或者是第i天刚好选择买,那现金就是前一天不持有的现金-买股票的钱
dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]) 继承或者前一天还持有,但是今天卖出去了
初始化
dp[0][0]=-prices[i]
dp[0][1]=0
"""

from typing import List

class Solution():
    def maxProfit(self,prices:List[int])->int:
        if len(prices)==0:
            return 0

        #dp数组
        dp=[[0]*2 for _ in range(len(prices))]

        #初始化
        dp[0][0]=-prices[0]
        dp[0][1]=0

        for i in range(1,len(prices)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        # print(dp)
        return dp[-1][1]


prices=[7,1,5,3,6,4]
solution=Solution()
print(solution.maxProfit(prices))

