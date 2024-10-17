"""
你是专业的小偷,计划偷窃沿街的房屋,每间房内都藏有一定的现金,影响你偷窃的惟一制约因素就是相邻的房屋装有相互连接的防盗系统,如果两间相邻的房间在同一晚上被小偷闯入,系统会自动报警
给定一个代表每个房屋存放金额的非负整数数组,计算你一夜之间能够偷窃到的最高金额.
"""

"""
dp[i] 到第i间房后能得道的最大金额为dp[i]
dp[i]=max(dp[i-1],dp[i-2]+value[i-1])
初始化的话:  dp[1]=value[0] dp[2]=value[1]
遍历顺序:顺序
"""
from typing import List

class Solution():
    def rob(self,value:List[int])->int:
        #特殊
        if len(value)<3:
            return max(value)
        #dp数组
        dp=[0]*(len(value)+1)
        #初始化
        dp[1]=value[0]
        dp[2]=max(value[0],value[1]) #重点

        for i in range(3,len(value)+1):
            dp[i]=max(dp[i-1],dp[i-2]+value[i-1])
        print(dp)
        return dp[len(value)]

# value=[1,2,3]
value=[ 2, 1, 1, 2]

solution=Solution()
print(solution.rob(value))

