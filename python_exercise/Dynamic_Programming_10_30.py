"""
给定字符串s和t，判断s是否为t的子序列
字符串的子序列是原始字符删除一些也可以不删除字符而不改变剩余字符相对位置形成的新字符串

输入 s='abc' t='ahbgdc'
输出 true

不变顺序，没有说是要求连续,这不又是最大重复子序列?
dp[i][j] 从0-s[i-1] 和0-t[j-1]的最大重复子序列长度为dp[i][j]
if s[i-1]==t[i-1]:
    dp[i][j]=dp[i-1][j-1]+1
else:
    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
if dp[i][j]=len(s)
    reuturn True
return False
这个效率太低了!!!
"""


class Solution():
    def isSubsequence(self,s:str,t:str)->bool:
        if len(s)==0:
            return True
        #dp
        dp=[[0]*(len(s)+1) for _ in range(len(t)+1)]

        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        if dp[-1][-1]==len(s):
            return True
        return False


"""
双指针
"""

class Solution():
    def isSubsequence(self,s:str,t:str)->bool:
        if len(s)==0:
            return True
        cur=0
        for i in range(len(t)):
            if t[i]==s[cur]: 
                cur+=1
            if cur==len(s):
                return True
        return False
        












