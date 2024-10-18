"""
给定一个数组prices,它的第i个元素prices[i]表示一支给定股票第i天的价格
你只能选择某一天买入这只股票,并选择在未来的某一天不同的日子卖出该股票.设计一个算法来计算你所能获得的最大利润
返回利润,如果没有任何利润,返回0
输入:[7,1,5,3,6,4]
输出:5
"""

"""直接想到的方法"""
from typing import List

class Solution():
    def maxProfit(self,nums:List[int])->int:
        if len(nums)==0:
            return 0
        result=0
        low=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]: #下降沿
                low=min(low,nums[i])
            elif nums[i]>nums[i-1]: #上升沿
                result=max(result,(nums[i]-low))
        return result

"""
利用动态规划解决所有的股票问题
dp[i][0] :第i天持有这支股票的最多现金
dp[i][1] :第i天不持有这支股票的最多现金
这里的持有,不代表买入,他可以表示i天才买入,也可以之前就买入了,i天还没抛售
同理,不持有不代表第i天才抛售,可以是之前就抛售了,或者一直没买股票,或者i天抛售

所以遍历到第i天时候:
dp[i][0]=max(dp[i-1][0],-prices[i]) 一个是继承昨天的状态,一个是今天买了,所以现金扣掉,谁让我现金最多,我就选哪个
dp[i][1]=max(dp[i-1][1],prices[i]+dp[i-1][0]) 一个继承昨天的状态,一个是今天才抛售,那就是现金+卖出的钱
初始化
dp[0][0]=-prices[0]
dp[0][1]=0
"""
class Solution1():
    def maxProfit(self,nums:List[int])->int:
        if len(nums)==0:
            return 0
        #dp数组
        dp=[[0]*2 for _ in range(len(nums))]
        print(dp)

        #初始化
        dp[0][0]=-nums[0]
        dp[0][1]=0

        for i in range(1,len(nums)):
            dp[i][0]=max(dp[i-1][0],-nums[i])
            dp[i][1]=max(dp[i-1][1],nums[i]+dp[i-1][0])

        return dp[-1][1] #不持有肯定>持有

nums=[7,1,5,3,6,4]
solution=Solution1()
print(solution.maxProfit(nums))
