"""
一个机器人位于mxn的网络的左上角,机器人每次只能向下或者向右移动一步,机器人试图达到网络的右下角,问总共有多少条不同的路径
"""

"""
动态规划5步骤
1. dp[m][n]的含义和下标定义:  m行n列位置的路径有dp[m][n]种
2. 递推公式:  dp[m][n]=dp[m-1][n]+dp[m][n-1]
3. dp数组如何初始化 :  dp[0][]=1 dp[][0]=1
4. 遍历顺序 :  从左上角到右下角
5. 打印dp数组 
"""


class Solution():
    def uniquePaths(self,m:int,n:int)->int:
        # dp数组
        dp=[[0]*n for _ in range(m)]
        # 初始化第一列
        for i in range(m):
        # 初始化第一行
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        
        for row in range(1,m):
            for col in range(1,n):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
        # print(dp)
        return dp[m-1][n-1]


m=3
n=7
solution=Solution()
print(solution.uniquePaths(m,n))
