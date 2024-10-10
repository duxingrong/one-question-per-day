"""
给定一个整数n,求以1...n为节点组成的二叉搜索树有多少种?
"""

"""
动态规划5步骤
1. dp[i]的含义和下标定义:   dp[i]表示以整数1...i为节点的二叉搜索树的个数
2. 递推公式:  dp[i]+=dp[j-1]*dp[i-j]  for j in range(1,i+1)
3. dp数组如何初始化 : dp[0]=1 dp[1]=1 
4. 遍历顺序 :  顺序
5. 打印dp数组 
"""


class Solution():
    def numTrees(self,n:int)->int:
        # 题目默认是2开始,所以不用考虑特殊情况

        # dp数组
        dp=[0]*(n+1)
        # 初始化
        dp[0]=1  # 这里主要是后面时乘法,所以得取1,它没有实际意义
        dp[1]=1

        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        print(dp)
        return dp[n]

n=4
solution=Solution()
print(solution.numTrees(n))
