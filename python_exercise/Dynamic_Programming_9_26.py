"""
爬楼梯,需要n阶才能到楼顶
每次可以是一或者二个台阶,有多少种不同的方法爬到楼顶
"""

"""
动态规划5步骤
1. dp[i]的含义和下标定义: 表示i阶楼梯的方式有dp[i]种
2. 递推公式: 
这里其实也是最需要搞懂的地方,我们如何才能到第三阶,只有两种可能,从第一阶走两步,从第二阶走一步.所以dp[3]=dp[1]+dp[2]
这就是斐波那契
3. dp数组如何初始化 : dp[1]=1, dp[2]=2
4. 遍历顺序 : 从左到右
5. 打印dp数组 
"""


class Solution():
    def climbStairs(self,n:int)->int:
        if n<3:
            return n
        dp=[1,2]
        for i in range(3,n+1):
            val=dp[1]
            dp[1]=dp[0]+dp[1]
            dp[0]=val
        return dp[1]



class Solution():
    def climbStairs(self,n:int)->int:
        if n<3:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

