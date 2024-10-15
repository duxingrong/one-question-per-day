"""
给定正整数n.找到若干个完全平方数(比如1,4,9,16...)使得它们的和等于n,需要让组成和的完全平方数的个数最少.
给你一个整数n,返回和为n的完全平方数的最少数量
"""

"""
还是一样的套路:首先是完全背包.然后是组合.
dp[j]把容量j装满的最少完全平方个数为dp[j]
遍历到物品i时候.如果不选,那就是dp[i-1]压缩成dp[j] .如果选,那dp[j]=dp[j-weight[i]]+1-->dp[j]=min(dp[j],dp[j-weight[i]]+1)
初始化dp[0]=0 dp=[0]*(n+1)
"""

class Solution():
    def numSquares(self,n:int):
        dp=[float('inf')]*(n+1)
        dp[0]=0
        #开始遍历
        for i in range(1,int(n**0.5)+1):
            for j in range(i*i,n+1):
                dp[j]=min(dp[j],dp[j-i*i]+1)
        if dp[n]==float('inf'):
            return -1
        return dp[n]

