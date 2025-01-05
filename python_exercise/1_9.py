"""
通配符匹配

给你一个输入字符串(s)和一个字符模式(p),请你实现一个支持'?'和'*'匹配规则的通配符匹配:
'?'可以匹配任何单个字符
'*'可以匹配任意字符序列(包括空字符序列)

判定匹配成功的充要条件是: 字符模式必须能够完全匹配输入字符串(而不是部分匹配)
"""

class Solution:
    def isMatch(self,s:str,p:str)->bool:
        """
        动态规划,化整为0
        dp[i][j] 表示s[:i]和p[:j]是否匹配
        """
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
        ## 初始化
        dp[0][0]=True
        ## 由"*"的特性,有的初始化为True
        for j in range(1,len(p)+1):
            if p[j-1]=="*":
                dp[0][j]=True
            else:
                break

        ## 开始遍历
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                if p[j-1]=="*": ## 当作空字符或者 去匹配多个字符
                    dp[i][j]= dp[i][j-1] or dp[i-1][j]

        return dp[-1][-1]

        
        
        
