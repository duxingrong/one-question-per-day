"""
给定一个正整数n,将其拆分为至少两个正整数的和,并使这些整数的乘积最大化,返回你可以获得的最大乘积

????这和动态规划有什么关系????

这个真难想到
"""

"""
动态规划5步骤
1. dp[i]的含义和下标定义:   dp[i]表示拆分i得到的最大乘积值
2. 递推公式:  dp[i]=max(j*(i-j),j*dp[i-j]) 拆分成两个,选择继续拆或者就两个数
3. dp数组如何初始化 : dp[2]=1
4. 遍历顺序 :  顺序
5. 打印dp数组 
"""
from typing import Optional

class Solution():
    def integerBreak(self,n:int)->Optional[int]:
        if n<2:
            return None

        # 初始化数组
        dp=[0]*(n+1)
        dp[2]=1

        # 开始拆分
        for i in range(3,n+1): # i从3到n,因为题目中是从2,而2作为了初始化
            for j in range(1,i//2+1): # 到一半就好了,由和定积最大可知
                dp[i]=max(dp[i],j*(i-j),j*dp[i-j]) # 这里加上dp[i]是因为j取不同数字的时候,最大值要一直更新最大
        return dp[n]




