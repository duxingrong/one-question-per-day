"""
140.单词拆分||

给定一个字符串s和一个字符串字典wordDict,在字符串s中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序返回所有这些可能的句子。

注意:词典中的同一个单词可能在分段中被重复使用多次。

递归+回溯+记忆化
"""

from typing import List

class Solution:
    def wordBreak(self,s:str,wordDict:List[str])->List[str]:
        # 将wordDict 转换为集合，便于0(1)复杂度查找
        word_set = set(wordDict)
        memo  = {} #记忆化，存储从某个位置到末尾的所有句子组合

        # 回溯函数
        def backtrack(start:int)->List[str]:
            # 如果起始位置已经在memo中，直接返回
            if start in memo:
                return memo[start]

            # 如果到达字符串末尾，返回空字符串，表示一种拆分完成
            if start == len(s):
                return [""]
            
            res = []
            # 遍历从start开始的所有可能的单词
            for end in range(start+1,len(s)+1):
                word = s[start:end]
                if word in word_set: # 如果单词在字典中
                    # 递归处理剩余部分
                    sub_sentences = backtrack(end)
                    # 将当前单词和后续句子组合
                    for sub in sub_sentences:
                        sentence = word +("" if not sub else " "+sub)
                        res.append(sentence)
            # 将结果存如memo,避免重复计算
            memo[start]=res
            return res
        # 调用回溯函数从位置0开始
        return backtrack(0)

# 测试用例
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

solution = Solution()
result = solution.wordBreak(s, wordDict)
print(result)  # 输出: ["cat sand dog", "cats and dog"]
