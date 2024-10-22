"""
我们在两条独立的水平线上按给定的顺序写下A和B的整数
现在，我们可以绘制一些连接两个数组A[i]和B[j]的直线，只要A[i]==B[j],且我们绘制的直线不与任何其他连线(非水平线相交)
以这种方法绘制线条，并返回我们可以绘制的最大连接数

例如: 
[1.4,2]
 |  \
[1,2,4]
这里连线不能交叉，实际上就是代表求的是不能改变相对顺序的最长公共子序列(一模一样)

dp[i][j] 0-i-1的A和0-j-1的B，他们的最长公共子序列的个数为dp[i][j]
 if A[i-1]==B[j-1] dp[i][j] =dp[i-1][j-1]+1
 else  dp[i][j]=max(dp[i-1][j],dp[i][j-1])

 dp[0][]=dp[][0]=0
"""

from typing import List

class Solution():
    def maxUncrossedLines(self,A:List[int],B:List[int])->int:
        if len(A)==0 or len(B)==0:
            return 0
        dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
        for i in range(1,len(B)+1):
            for j in range(1,len(A)+1):
                if A[j-1]==B[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

A=[1,2,4]
B=[1,4,2]
solution=Solution()
print(solution.maxUncrossedLines(A,B))
