"""
给定一个非空字符串s和一个包含非空单词的列表wordDict.判定s是否可以被空格拆分为一个或多个在字典中出现的单词

这个题目其实也是看这些特别的单词(物品)能不能把这个s(背包装满)?难点在于想出dp的含义和第推公式
dp[j]的含义: 长度为j的字符串如果在单词列表里面.则dp[j]为true.如果不在,那dp[j]=false
这个题目因为是特定的背包.所以对顺序有要求,是排序问题->先遍历背包.再遍历物品

for j in range(1,len(s)+1)对于背包j的时候: for i in range(0,j+1): if s[i:j] in wordDict and dp[i]==true: dp[j]=true 
通俗来说就是满足此时的s[i,j]在字典里并且前面的s[0,i]也在字典里.那就可以推出dp[j]是true
边界的话用实例来演示就知道了 比如s='applepenapple' wordDict=['apple','pen']
所以dp[5](长度为5的字符串在不在的bool值为dp[5]).即'apple',此时内层i=0时.s[0:5]是'apple'在 并且 dp[i]=dp[0]=true)
所以dp[5]=true
初始化: dp[0]=true 才满足第推条件.不然不会有任何一个等于true
"""
from typing import List

class Solution():
    def wordBreak(self,s:str,wordDict:List[str])->bool:
        #dp数组
        dp=[False]*(len(s)+1)
        dp[0]=True

        for j in range(1,len(s)+1):
            for i in range(0,j+1):
                if s[i:j] in wordDict and dp[i]==True:
                    dp[j]=True
        print(dp)
        return dp[len(s)]

s='applepenapple'
wordDict=['apple','pen']
solution=Solution()
print(solution.wordBreak(s,wordDict))
