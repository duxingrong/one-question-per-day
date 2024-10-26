"""

给定一个字符串，计算出这个字符串中有多少个回文子串
具有不同位置或结束位置的子串，即使是由相同的字符串组成，也会被视作不同的回文子串

例如: 'aaa'
输出:6
'a' 'a' 'a' 'aa' 'aa' 'aaa'

这个题目是连续的
dp数组的含义: dp[i][j] [i,j+1]这个子串是不是回文子串
这里确实需要用分而治之的思想

dp[i][j]
1. 如果j==i: 那就说明s[i:j+1]只有一个数，那肯定是回文串
2. 如果s[i]==s[j],那么dp[i][j]=dp[i+1][j-1] 意思就最外面的左右两个是相等的，如果它们中间的部分也是回文串的话，那s[i:j+1]就是回文串
3. 如果s[i]!=s[j]，那就一定不是dp[i][j]=False

从第推公式我们可以知道dp[i][j] 需要dp[i+1][j-1]
位置关系:
^   dp[i][j-1]   dp[i][j]
|   dp[i+1][j-1] dp[i+1][j]
--->
所以遍历顺序是i 逆序，j顺序
"""

class Solution():
    def countSubstrings(self,s:str)->int:
        if len(s)==0:
            return 0
        #dp数组
        dp=[[False]*(len(s)) for _ in range(len(s))]
        result=0

        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):#要保证s[i:j+1]有意义
                if s[i]==s[j] and(j-i<=1 or dp[i+1][j-1]):
                    result+=1
                    dp[i][j]=True
        return result



"""
双指针最慢了
"""
class Solution():
    def countSubstrings(self,word:str)->int:
        if len(word)<=1:
            return len(word)
        
        def is_true(word:str):
            if word[::-1]==word:
                return True
            return False
        #双指针
        result=0
        for i in range(len(word)): #结尾
            for j in range(i+1):
                if is_true(word[j:i+1]) :
                    # print(word[j:i+1])
                    result+=1

        return result

solution=Solution()
word='aaa'
print(solution.countSubstrings(word))


