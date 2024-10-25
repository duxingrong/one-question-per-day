"""
给定两个单词word1和word2,找到使得word1和word2相同所需要的最小步数，每步可以删除任意一个字符串的任意一个字符


例如: word1='sea' word2='eat'
输出: 2
第一步将sea变成 ea
第二步将eat变成 ea

dp[i][j] 0到i-1的word1和0到j-1的word2,相同所需要的最少步数为dp[i][j]

if word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1] #相当于白嫖
else:
    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1

然后初始化?要问怎么知道的就是从下面的这个表格
dp[0][0]=0
dp[i][0]=i
dp[0][j]=j


0  1  2  3 
1  2  1  2

2  3  2  1

3  4  3  2
"""

class Solution():
    def minDistance(self,word1:str,word2:str)->int:
        #dp数组
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        #初始化
        for i in range(1,len(word1)+1):
            dp[i][0]=i
        for j in range(1,len(word2)+1):
            dp[0][j]=j

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]

word1='leetcode'
word2='etco'
solution=Solution()
print(solution.minDistance(word1,word2))
