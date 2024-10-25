"""
给你两个单词word1和word2,请你计算出将word1转换成word2所使用的最少操作数
你可以对一个单词进行下面三种操作
1. 输入一个字符
2. 删除一个字符
3. 替换一个字符

输入 word1="horse" word2="ros"
输出: 3
horse->rorse->rose->lros

这里要怎么理解呢?这三种操作其实都算一步骤，但是我怎么让机器理解呢我现在的word1是什么样子呢?

这里秒就秒在我们对word1进行添加操作，不就是相当于对2进行了删除操作马？这样的话和上一个题目唯一的区别就是有了一个替换，这个我们在第推的时候就知道怎么使用了

if word1[i-1]==word2[j-1]:
    那就是相当于延续前面的状态，因为新遍历的这两个值等于没有 dp[i][j]=dp[i-1][j-1]
else:
    1. 我删去这个新的值 dp[i-1][j]+1
    2. 我添加一个值，等于我删去word2: dp[i][j-1]+1
    3. 我不删，我进行替换变成一样的后，不是又回到了相等的状态吗?  相当于比相等的时候多了一步替换 dp[i-1][j-1]+1
    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

这里秒就妙在对题目意思的转换上
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
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        # print(dp)
        return dp[-1][-1]


word1="horse" 
word2="ros"

solution=Solution()
print(solution.minDistance(word1,word2))









