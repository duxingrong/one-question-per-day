"""
给两个整数数组A和B，返回两个数组中公共的，长度最长的子数组的长度
这里所说的子数组，其实就是连续子序列
"""

"""
这里最难的其实还是dp数组的定义
dp[i][j] 以[i-1]结尾的A，和以[j-1]结尾的B，最长重复子序列的长度为dp[i][j]

第推
for i in range(1,len(A)+1):
for j in range(1,len(B)+1):
    if A[i-1]=B[j-1]:
        dp[i][j]=dp[i-1][j-1]+1

初始化: dp[0][] =dp[][0]=0 第一行第一列都是没有实际意义的，只需要为第推公式服务
遍历顺序:两层顺序无所谓，数组优先级一致

"""

from typing import List

class Solution():
    def findLength(self,A:List[int],B:List[int])->int:
        if len(A)==0 or len(B)==0:
            return 0
        #dp数组和初始化
        dp=[[0]*(len(A)+1) for _ in range(len(B)+1)]
        result=0
        
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    result=max(result,dp[i][j])
        return result


A=[1,2,3,2,1]
B=[3,2,1,4,7]
solution=Solution()
print(solution.findLength(A,B))
