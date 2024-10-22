"""

给定两个字符串text1和text2,返回这两个字符串的最长公共子序列的长度

一个字符串的子序列是指这样一个新的字符串，它是由原字符串在不改变字符的相对顺序的情况下删除某些字符(也可以不删除任何字节)后组成的新子字符串

输入: text1="abcde" text2='ace'
输出: 3

这里的难点还是dp数组的定义:
求递增序列的时候，因为要求序列有序，所以必须确定序列的最后一个元素的值，才能比较新加入序列的元素是不是递增的。
求想等序列的时候，如果求连续想等的子序列，则还是要确定序列最后一个元素的值；但是本题求的是不必连续的想等子序列，就不需要知道序列最后一个元素的值，只要知道范围内相等的序列长度就行，新来的相等元素直接加在后面就好

dp[i][j] 0到i-1的text1和0到j-1的text2 的公共最长子序列长度为dp[i][j]

for i in range(1,len(text1)+1):
for j in range(1,len(text2)+1):
if text1[i-1]==text2[j-1]: dp[i][j]=dp[i-1][j-1]    
else: 
    dp[i][j] =max(dp[i-1][j],dp[i][j-1]) 如果当前字符不相等，我们不能将它们加入公共子序列，而是从忽略其中一个字符的两种情况中选择最长的子序列继续 


第推公式知道dp[][0]=dp[0][]=0  没有实际意义
"""

class Solution():
    def longestCommonSubsequence(self,text1:str,text2:str)->int:
        if len(text1)==0 or len(text2)==0:
            return 0
        #dp数组
        dp=[[0]*(len(text1)+1) for _ in range(len(text2)+1)]

        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                if text2[i-1]==text1[j-1]:  #想等
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        

text1='abcde'
text2='abc'

solution=Solution()
print(solution.longestCommonSubsequence(text1,text2))







