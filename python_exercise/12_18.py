"""
最长回文子串

给你一个字符串s,找到s中最长的回文子串
s='babad' 输出='bab'

s='cbbd' 输出= 'bb'
"""

"""
动态规划:
定义：
布尔类型的dp[i][j]:表示区间范围[i,j](左闭右闭)的子串是否是回文子串,如果是dp[i][j]为true,否则为false.
递归公式: 
1.s[i]!=s[j],那就没什么讨论的,dp[i][j]一定是false 
2.s[i]==s[j],那么又要分类:
    - 如果i==j,那么说明是同一个字符,自然dp[i][j]是回文子串
    - 如果j-i=1,例如aa,那也说明是一个回文子串
    - else 那么dp[i][j]是否为回文子串,取决于dp[i+1][j-1],即成功递推

遍历顺序:
由递推公式,推出遍历顺序为,i为倒序遍历,j为正序遍历

初始化:
开局全为false 

"""

class Solution():
    def longestPalindrome(self,s:str)->str:
        #构造dp数组
        n= len(s)
        dp = [[False]*n for _ in range(n)]

        #记录最大的长度
        maxlen = 0
        left = 0
        
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j]:
                    if i==j: dp[i][j]=True
                    elif j-i==1: dp[i][j]=True 
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j]=False

                #更新最大长度
                if dp[i][j] and j-i+1 >maxlen:
                    maxlen = j-i+1 
                    left = i 
                
        return s[left:left+maxlen]
    
if __name__ == "__main__":
    s='a'
    solution = Solution()
    print(solution.longestPalindrome(s))

            




