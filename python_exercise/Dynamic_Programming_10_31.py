"""
给定一个字符串s和一个字符串t，计算s的子序列中t出现的个数

输入: s='rabbbit' t='rabbit'
输出: 3

求子序列(不用连续),但是这题目求的是特定子序列的个数

dp[i][j] 0到i-1的s中有0到j-1的t的个数为dp[i][j]

两层for循环:
    if s[i-1]==t[j-1]: 这时候就有意思了例如t是bag,s是babga ,此时t又来了一个g，那现在新的t含有bag的数量是在原来的t=babga含有bag的树量上dp[i-1][j]增加了使用新来的g新组成的bag,而新来的能组成多少个bag，取决于原来的t能组成多少个ba(dp[i-1][j-1])
    else: 不相等 那dp[i][j]=dp[i-1][j] 因为加上你没有，你组成不了任何的s，所以有你等于没有dp[i][j]=dp[i-1][j],还是原来多少个就是多少个

初始化 
dp[0][]=0 s都是空集了，当然在s中出现的个数为0
dp[][0]=1 t为空集，那s只有删光和他匹配，一种
dp[0][0]?  由dp[1][1]=dp[0][0]+dp[0][1]=1 -->dp[0][0]=1

"""


class Solution():
    def numDistinct(self,s:str,t:str)->int:
        #dp数组
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        #初始化
        for i in range(len(t)+1):
            dp[0][i]=0
        for j in range(len(s)+1):
            dp[j][0]=1

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]: 
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[-1][-1]

s='rabbbit'
t='rabbit'
solution=Solution()
print(solution.numDistinct(s,t))

