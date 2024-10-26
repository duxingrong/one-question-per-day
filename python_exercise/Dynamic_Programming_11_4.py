"""
给定一个字符串s，找到其中最长的回文子序列，并返回该序列的长度，可以假设s的最大长度是1000

输入: 'bbbab'
输出'bbbb'
输入: 'cbbd'
输出: 'bb'


dp[i][j]: s[i,j+1](左闭右开)的区间的最长回文子串的个数

dp[i][j]: 
if s[i]=s[j]: 那就是dp[i][j]=dp[i+1][j-1]+2
else:
    考虑左边最大的和考虑右边最大的取最大值max(dp[i][j-1],dp[i+1][j])

初始化,由第推公式可以看出，根基是dp[i][i]即i==j的时候，初始为1

由第推公式 遍历顺序为i逆序,j顺序

"""

class Solution():
    def longestPalindromeSubseq(self,s:str)->int:
        if len(s)==0:
            return 0
        #dp数组
        dp=[[0]*(len(s)) for _ in range(len(s))]
        #初始化
        for i in range(len(s)):
            dp[i][i]=1

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]








