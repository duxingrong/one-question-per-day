"""
分割回文串||

给你一个字符串s,请你将s分割成一些子串，使每个子串都是回文.
返回符合要求的最少分割次数.

s='aab' 输出1,解释:只需要一次分割就可以将s分割成['aa','b']这样的两个回文子串
"""


"""
难点依旧还是动态规划

定义:
dp[i] : 表示[0,i]闭区间内的字符串成回文串的最少次数为dp[i].

递推:
dp[i]: 取中间点j,如果dp[j+1,i]是回文串,那直接就有dp[i]=dp[j]+1
    从公式可以看出，j可以取0到i-1,所以dp[i]=min(dp[i],dp[j]+1)
或者[0,i]就是回文串，那就直接dp[i]=0

遍历顺序: 顺序就好

初始化,由于是最小值,所以初始化为sys.maxsize
"""

import sys

class Solution():
    def minCut(self,s:str)->int:

        #首先是判断每个区间是否是回文串
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if i==j or j-i==1:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False

        #然后开始判断最少切割几次
        res = [sys.maxsize]*n

        for i in range(n):
            #是回文直接返回
            if dp[0][i]:
                res[i]=0
            #来遍历中间值 
            for j in range(0,i):
                if dp[j+1][i]:
                    res[i]=min(res[i],res[j]+1)

        return res[-1] #也就是res[n-1]

if __name__=="__main__":
    s='aabbc' 
    solution =Solution()
    print(solution.minCut(s))
    

